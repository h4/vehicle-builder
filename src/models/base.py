from dataclasses import dataclass, fields
from functools import reduce
from itertools import chain
from typing import ClassVar, Dict, Iterable
import sqlalchemy as sa
from more_itertools import always_iterable, first
from sqlalchemy.util import classproperty
from sqlalchemy.dialects.postgresql import (array_agg,
                                            aggregate_order_by)


class ToManyRelation:
    def __init__(self, tables, *, column=None, order=None, label=None,
                 join_on=None):
        self._tables = list(always_iterable(tables))
        self._label = label

        self._from = reduce(lambda x, y: x.join(y), self._tables)
        if self._label is not None:
            self._from = self._from.alias(self._label)

        if column is not None:
            self.column = column
        else:
            if len(self._tables) > 1:
                raise ValueError('For multi-table-joined relations `column` should be specified')
            self.column = self._tables[0].c.id

        if order is not None:
            self._order = order
        else:
            self._order = self.column.asc().nullslast()

        self._join_on = join_on

        self.aggregated = array_agg(aggregate_order_by(self.column, self._order))
        # TODO: select only required columns?

    def join_relation(self, selectable):
        return selectable.outerjoin(self._from, self._join_on)


@dataclass
class Model:
    _tablename: ClassVar[sa.Table] = None
    _pk: ClassVar[str] = 'id'
    _to_one_relations: ClassVar[Dict[str, sa.Table]] = {}
    _to_many_relations: ClassVar[Dict[str, ToManyRelation]] = {}
    _extra_columns: ClassVar[Iterable[sa.Column]] = []

    @classproperty
    def table(cls):
        return getattr(cls, '_table')

    @classproperty
    def c(cls):
        return cls.table.c

    @classproperty
    def fields(cls):
        return [f.name for f in chain(fields(cls), cls._extra_columns)]

    @classmethod
    def get_column(cls, column):
        if isinstance(column, sa.Column):
            return column
        return getattr(cls.table.c, column)

    @classproperty
    def pk_column(cls):
        return cls.get_column(cls._pk)

    @classproperty
    def default_selectable(cls):
        selectable = cls.table
        for relation in cls._to_many_relations.values():
            selectable = relation.join_relation(selectable)
        return selectable

    @classproperty
    def to_many_selectables(cls):
        for field, relation in cls._to_many_relations.items():
            yield relation.aggregated.label(field)

    @classmethod
    def query(cls, where=None):
        query = cls.default_selectable.select(use_labels=True)
        if where is not None:
            query = query.where(where)
        return query

    @classmethod
    async def fetch_many(cls, query=None, filter_by=None):
        from asyncpgsa import pg

        columns = [*cls.c, *cls.to_many_selectables]

        filter_expressions = []
        result = []

        if filter_by is not None:
            for column_name, filter_rule in filter_by.items():
                try:
                    column = getattr(cls.c, column_name)
                except AttributeError:
                    raise ValueError(f'Table `{cls.table.name}` does not '
                                     f'contain column `{column_name}`')

                filter_expressions.append((column == filter_rule))

        if query is None:
            query = cls.query()

        if filter_expressions:
            query = query.where(sa.and_(*filter_expressions))

        if len(cls._to_many_relations):
            query = query.group_by(cls.pk_column)

        query = query.with_only_columns(columns)

        async with pg.query(query) as cursor:
            async for row in cursor:
                resource = cls.from_row(row, columns=columns)
                result.append(resource)
        return result

    @classmethod
    async def fetch_by_ids(cls, ids):
        return await cls.fetch_many(
            query=cls.query(where=cls.pk_column.in_(list(always_iterable(ids))))
        )

    @classmethod
    async def fetch_one(cls, pk):
        results = await cls.fetch_by_ids([pk])
        return first(results, None)

    @classmethod
    def from_row(cls, row, exclude=(), columns=None, **kwargs):
        if not row:
            return None
        if columns is None:
            columns = cls.table.c

        initial_data = {column.name: row[column._key_label]
                        for column in columns
                        if column.name in cls.fields
                        and column.name not in exclude}
        initial_data.update(kwargs)
        result = cls(**initial_data)
        return result
