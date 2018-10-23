from dataclasses import dataclass, field
from decimal import Decimal
from typing import ClassVar, Dict, List, Optional

from sqlalchemy import Table

from db import tables
from models.base import Model, ToManyRelation


@dataclass
class Component(Model):
    _table: ClassVar[Table] = tables.components
    _to_many_relations: ClassVar[Dict[str, ToManyRelation]] = dict(
        properties=ToManyRelation(tables.component_properties)
    )

    title: str
    cad_model: str
    sku: str
    provider: str
    weight: Decimal
    price: Decimal
    properties: List['ComponentProperty'] = field(default_factory=list)
    id: Optional[int] = None


@dataclass
class ComponentProperty(Model):
    _table: ClassVar[Table] = tables.component_properties

    property_name: str
    value: str
    component_id: int
    id: Optional[int] = None
