from dataclasses import dataclass
from typing import ClassVar, Optional

from sqlalchemy import Table

from db import tables
from models.base import Model


@dataclass
class Interface(Model):
    _table: ClassVar[Table] = tables.interfaces

    title: str
    id: Optional[int] = None
