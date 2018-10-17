from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto


class ProductionStatus(Enum):
    DESIGN = auto()
    PRODUCTION = auto()
    ORDERED = auto()
    IN_STOCK = auto()
    DEPRECATED = auto()


@dataclass
class Component:
    title: str
    cad_model: str
    sku: str
    provider: str
    weight: float
    price: Decimal
    status: ProductionStatus


@dataclass
class ComponentProperty:
    title: str
    value: any
