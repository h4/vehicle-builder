from enum import unique, Enum, auto


@unique
class ProductionStatus(Enum):
    UNKNOWN = auto()
    DESIGN = auto()
    PRODUCTION = auto()
    ORDERED = auto()
    IN_STOCK = auto()
    DEPRECATED = auto()
