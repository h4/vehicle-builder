from decimal import Decimal

from entities.components import Component, ComponentProperty


class TestComponents:
    def test_can_add_property(self):
        component = Component('Component', 'cad', 'sku', 'abc', 1.0, Decimal(1.0))
        prop = ComponentProperty('Prop Name', 1)

        component.add_property(prop)

        assert len(component.properties) > 0

    def test_properties_are_unique(self):
        component = Component('Component', 'cad', 'sku', 'abc', 1.0, Decimal(1.0))
        prop_1 = ComponentProperty('Prop Name 1', 1)
        prop_2 = ComponentProperty('Prop Name 2', 2)

        component.add_property(prop_1)
        component.add_property(prop_2)
        component.add_property(prop_1)

        assert len(component.properties) == 2
