from dataclasses import dataclass, field
from typing import ClassVar, Dict, List, Optional

from sqlalchemy import Table

from db import tables
from models.base import Model, ToManyRelation


@dataclass
class Vehicle(Model):
    _table: ClassVar[Table] = tables.vehicles
    _to_many_relations: ClassVar[Dict[str, ToManyRelation]] = dict(
        properties=ToManyRelation(tables.vehicle_properties)
    )

    title: str
    range: int
    properties: List = field(default_factory=list)
    id: Optional[int] = None


@dataclass
class VehicleProperty(Model):
    _table: ClassVar[Table] = tables.vehicle_properties

    property_name: str
    value: str
    vehicle_id: int
    id: Optional[int] = None
