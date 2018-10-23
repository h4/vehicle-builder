from dataclasses import dataclass, field
from typing import ClassVar, Dict, Optional, Iterable

import sqlalchemy as sa
from sqlalchemy import Table

from db import tables
from models.base import Model, ToManyRelation

tbl_children = tables.groups.alias('children')


@dataclass
class Group(Model):
    _table: ClassVar[Table] = tables.groups
    _to_one_relations: ClassVar[Dict[str, Table]] = dict(parent=tables.groups)
    _to_many_relations: ClassVar[Dict[str, ToManyRelation]] = dict(
        children=ToManyRelation(
            tbl_children,
            join_on=(sa.and_(tables.groups.c.id == tbl_children.c.parent_id))
        ),
        features=ToManyRelation(tables.features),
    )

    title: str
    parent_id: int
    path: str
    parent: Optional['Group'] = None
    children: Optional[Iterable['Group']] = field(default_factory=list)
    features: Optional[Iterable['Feature']] = field(default_factory=list)
    is_set: bool = False
    id: Optional[int] = None


@dataclass
class Feature(Model):
    _to_many_relations: ClassVar[Dict[str, ToManyRelation]] = dict(
        functions=ToManyRelation(tables.functions),
    )

    _table: ClassVar[Table] = tables.features
    title: str
    parent_id: int
    functions: Optional[Iterable['Feature']] = field(default_factory=list)
    id: Optional[int] = None


@dataclass
class Function(Model):
    _table: ClassVar[Table] = tables.functions
    title: str
    feature_id: int
    id: Optional[int] = None
