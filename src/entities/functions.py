from dataclasses import dataclass, field
from typing import List

from common.exceptions import ValidationError
from entities.base import BaseEntity


@dataclass
class Feature:
    title: str
    parent_group: 'Group' = None
    functions: List["Function"] = field(default_factory=list)

    def add_function(self, func: "Function"):
        self.functions.append(func)


@dataclass
class Group(BaseEntity):
    title: str
    features: List["Feature"] = field(default_factory=list)
    parent_group: "Group" = None
    is_set: bool = False
    subgroups: List["Group"] = field(default_factory=list)

    def add_feature(self, feature: "Feature"):
        feature.parent_group = self
        self.features.append(feature)

    @property
    def is_root_group(self):
        return self.parent_group is None

    def add_subgroup(self, child: "Group"):
        if child in self.subgroups:
            raise ValidationError('Already present')

        if child == self:
            raise ValidationError('Can\' add group to itself')

        child.parent_group = self
        self.subgroups.append(child)


@dataclass
class Function(BaseEntity):
    title: str
