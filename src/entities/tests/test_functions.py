import pytest

from common.exceptions import ValidationError
from entities.functions import Group, Feature, Function


class TestGroup:
    def test_can_add_feature_into_group(self):
        group = Group('New Group')
        feature = Feature('New Feature')
        group.add_feature(feature)

        assert feature in group.features

    def test_group_is_root_by_default(self):
        group = Group('New Group')
        assert group.is_root_group is True

    def test_add_subgroup(self):
        parent = Group('Parent Group')
        child = Group('Child Group')
        parent.add_subgroup(child)

        assert child.parent_group == parent
        assert child in parent.subgroups

    def test_can_not_add_subgroup_twice(self):
        parent = Group('Parent Group')
        child = Group('Child Group')
        parent.add_subgroup(child)
        with pytest.raises(ValidationError):
            parent.add_subgroup(child)

    def test_can_not_add_itself(self):
        parent = Group('Parent Group')
        with pytest.raises(ValidationError):
            parent.add_subgroup(parent)


class TestFeature:
    def test_can_add_function(self):
        feature = Feature('New Feature')
        func = Function('New Function')
        feature.add_function(func)

        assert func in feature.functions
