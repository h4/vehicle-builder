from dataclasses import dataclass
from typing import List

from entities.components import Component
from entities.iterfaces import Interface
from .functions import Feature, Function


@dataclass
class Vehicle:
    title: str
    range: int


@dataclass
class VehicleProperty:
    title: str
    value: any


@dataclass
class VehicleConfiguration:
    vehicle: "Vehicle"
    features: List[Feature]


@dataclass
class ComponentLink:
    component: Component
    interface: Interface


@dataclass
class VehicleFunctionConfiguration:
    vehicle: "Vehicle"
    function: Function
    components: List["ComponentLink"]
    is_frozen: bool = False
