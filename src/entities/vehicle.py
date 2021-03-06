from dataclasses import dataclass, field
from typing import List

from common.exceptions import ValidationError
from entities.base import BaseEntity
from entities.components import Component
from entities.iterfaces import Interface
from entities.functions import Feature, Function


@dataclass
class Vehicle(BaseEntity):
    title: str
    range: int
    properties: List["VehicleProperty"] = field(default_factory=list)

    def add_property(self, prop: "VehicleProperty"):
        if prop not in self.properties:
            self.properties.append(prop)


@dataclass
class VehicleProperty(BaseEntity):
    title: str
    value: any


@dataclass
class VehicleConfiguration(BaseEntity):
    vehicle: "Vehicle"
    features: List[Feature] = field(default_factory=list)
    functions: List["VehicleFunction"] = field(default_factory=list)

    def _add_function(self, func):
        vehicle_function = VehicleFunction(func)
        self.functions.append(vehicle_function)

    def add_feature(self, feature: Feature):
        self._validate_set_feature(feature)

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

    def _validate_set_feature(self, feature):
        if feature.parent_group is not None and feature.parent_group.is_set:
            for f in self.features:
                if f.parent_group == feature.parent_group:
                    raise ValidationError('Can\'t add two features from same set')


@dataclass
class VehicleFunction(BaseEntity):
    function: Function
    components: List["ComponentLink"] = field(default_factory=list)
    is_frozen: bool = False

    def add_component(self, component: "ComponentLink"):
        self.components.append(component)

    @property
    def is_fulfilled(self):
        return len(self.components) > 0 or self.is_frozen


@dataclass
class ComponentLink(BaseEntity):
    component: Component
    interface: Interface
