from abc import ABC, abstractmethod
from typing import List

from entities.vehicle import Vehicle


class VehicleRepositoryABC(ABC):
    @abstractmethod
    def save(self, vehicle: Vehicle): pass

    @abstractmethod
    def get_all(self) -> List[Vehicle]: pass

    @abstractmethod
    def find_by_id(self, pk: int) -> Vehicle: pass
