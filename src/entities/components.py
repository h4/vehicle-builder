from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum, auto
from typing import List

from entities.base import BaseEntity


class ProductionStatus(Enum):
    DESIGN = auto()
    PRODUCTION = auto()
    ORDERED = auto()
    IN_STOCK = auto()
    DEPRECATED = auto()


@dataclass
class Component(BaseEntity):
    title: str
    cad_model: str
    sku: str
    provider: str
    weight: float
    price: Decimal
    status: ProductionStatus = ProductionStatus.DESIGN
    properties: List["ComponentProperty"] = field(init=False, default_factory=list)

    def add_property(self, prop):
        if prop not in self.properties:
            self.properties.append(prop)


@dataclass
class ComponentProperty(BaseEntity):
    title: str
    value: any
