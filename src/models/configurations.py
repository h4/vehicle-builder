from dataclasses import dataclass, field
from typing import Optional, ClassVar, Dict, Iterable

import sqlalchemy as sa
from sqlalchemy import Table

from db import tables
from models.base import Model, ToManyRelation
from models.groups import Feature, Function


@dataclass
class Configuration(Model):
    _table: ClassVar[Table] = tables.vehicle_configurations
    _to_one_relations: ClassVar[Dict[str, Table]] = dict(
        vehicle=tables.vehicles)

    vehicle_id: int
    feature_id: int
    id: Optional[int] = None


@dataclass
class VehicleFunctions(Model):
    _table: ClassVar[Table] = tables.vehicle_functions
    _to_many_relations: ClassVar[Dict[str, ToManyRelation]] = dict(
        connections=ToManyRelation(tables.vehicle_connections),
        functions=ToManyRelation(tables.functions),
        features=ToManyRelation(tables.features, join_on=(
            sa.and_(
                tables.vehicle_functions.c.function_id == tables.functions.c.id,
                tables.functions.c.feature_id == tables.features.c.id,
            )
        )),
    )

    vehicle_id: int
    function_id: int
    connections: Optional[Iterable['VehicleConnections']] = field(
        default_factory=list)
    functions: Optional[Function] = None
    features: Optional[Feature] = None
    is_frozen: bool = False
    id: Optional[int] = None


@dataclass
class VehicleConnections(Model):
    _table: ClassVar[Table] = tables.vehicle_connections
    _to_one_relations: ClassVar[Dict[str, Table]] = dict(
        vehicle_function_id=tables.vehicle_functions
    )
    _to_many_relations: ClassVar[Dict[str, ToManyRelation]] = dict(
        components=ToManyRelation(tables.components),
        interfaces=ToManyRelation(tables.interfaces),
    )

    vehicle_function_id: int
    component_id: int
    interface_id: int
    is_frozen: bool = False
    id: Optional[int] = None
