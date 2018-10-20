from dataclasses import dataclass, field
from typing import Any


@dataclass
class BaseEntity:
    _id: Any = field(init=False)

    def __post_init__(self):
        self._id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
