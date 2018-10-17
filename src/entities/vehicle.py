from dataclasses import dataclass, field
from typing import List

from .components import Component
from .iterfaces import Interface
from .functions import Feature, Function


@dataclass
class Vehicle:
    title: str
    range: int
    properties: List["VehicleProperty"] = field(default_factory=list)

    def add_property(self, prop: "VehicleProperty"):
        if prop not in self.properties:
            self.properties.append(prop)


@dataclass
class VehicleProperty:
    title: str
    value: any


@dataclass
class VehicleConfiguration:
    vehicle: "Vehicle"
    features: List[Feature] = field(default_factory=list)
    functions: List["VehicleFunction"] = field(default_factory=list)

    def _add_function(self, func):
        vehicle_function = VehicleFunction(func)
        self.functions.append(vehicle_function)

    def add_feature(self, feature: Feature):
        if feature not in self.features:
            self.features.append(feature)
            for func in feature.functions:
                self._add_function(func)

    def link_component_to_function(self, func, component, interface):
        vehicle_function = next(f for f in self.functions if f.function == func)
        link = ComponentLink(component, interface)
        vehicle_function.add_component(link)

    @property
    def is_fulfilled(self):
        return all(f.is_fulfilled for f in self.functions)


@dataclass
class VehicleFunction:
    function: Function
    components: List["ComponentLink"] = field(default_factory=list)
    is_frozen: bool = False

    def add_component(self, component: "ComponentLink"):
        self.components.append(component)

    @property
    def is_fulfilled(self):
        return len(self.components) > 0 or self.is_frozen


@dataclass
class ComponentLink:
    component: Component
    interface: Interface
