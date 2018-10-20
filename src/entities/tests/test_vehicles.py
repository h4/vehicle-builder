from decimal import Decimal

import pytest

from common.exceptions import ValidationError
from entities.components import Component
from entities.iterfaces import Interface
from entities.functions import Feature, Function, Group
from entities.vehicle import Vehicle, VehicleProperty, VehicleConfiguration


class TestVehicle:
    def test_can_add_property_for_vehicle(self):
        vehicle = Vehicle('New Vehicle', 1000)
        prop = VehicleProperty('name', 'value')
        vehicle.add_property(prop)

        assert prop in vehicle.properties

    def test_avoid_duplicated_props(self):
        vehicle = Vehicle('New Group', 1000)
        prop_1 = VehicleProperty('name_1', 'value')
        prop_2 = VehicleProperty('name_2', 'value')
        vehicle.add_property(prop_1)
        vehicle.add_property(prop_2)
        vehicle.add_property(prop_1)

        assert prop_1 in vehicle.properties
        assert prop_2 in vehicle.properties
        assert len(vehicle.properties) == 2


class TestVehicleConfiguration:
    def test_returns_flatten_list_of_functions(self):
        vehicle = Vehicle('New Vehicle', 1000)
        feature_1 = Feature('Feature 1')
        func_1 = Function('Function 1')
        func_2 = Function('Function 2')
        feature_1.add_function(func_1)
        feature_1.add_function(func_2)
        feature_2 = Feature('Feature 2')
        func_3 = Function('Function 2')
        func_4 = Function('Function 3')
        feature_2.add_function(func_3)
        feature_2.add_function(func_4)

        configuration = VehicleConfiguration(vehicle)
        configuration.add_feature(feature_1)
        configuration.add_feature(feature_2)

        assert len(configuration.functions) == 4

    def test_can_not_add_two_features_from_set(self):
        vehicle = Vehicle('New Vehicle', 1000)
        feature_1 = Feature('Feature 1')
        feature_2 = Feature('Feature 2')
        features_set = Group('Set', is_set=True)
        features_set.add_feature(feature_1)
        features_set.add_feature(feature_2)
        configuration = VehicleConfiguration(vehicle)
        configuration.add_feature(feature_1)

        with pytest.raises(ValidationError):
            configuration.add_feature(feature_2)


class TestLinkComponentsToVehicle:
    def test_can_add_component(self):
        interface_1 = Interface('Interface 1')
        component_1 = Component('Component 1', 'cad', 'sku', 'provider', 0.1, Decimal(12.2))
        vehicle = Vehicle('New Vehicle', 1000)
        feature_1 = Feature('Feature 1')
        func_1 = Function('Function 1')
        feature_1.add_function(func_1)
        configuration = VehicleConfiguration(vehicle)
        configuration.add_feature(feature_1)

        assert configuration.is_fulfilled is False

        configuration.link_component_to_function(func_1, component_1, interface_1)

        assert configuration.is_fulfilled is True
