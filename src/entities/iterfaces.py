from dataclasses import dataclass

from entities.base import BaseEntity


@dataclass
class Interface(BaseEntity):
    title: str
