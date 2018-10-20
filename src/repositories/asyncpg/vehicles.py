from typing import List

from db.models.vehicles import VehicleModel
from db.tables import vehicles
from entities.vehicle import Vehicle
from repositories.abstract.vehicles import VehicleRepositoryABC


class VehiclePGRepository(VehicleRepositoryABC):
    def __init__(self, conn):
        self.conn = conn

    async def find_by_id(self, pk: int) -> Vehicle:
        query = vehicles.select().where(vehicles.c.id == pk)
        async with self.conn.query(query) as cursor:
            async for row in cursor:
                return VehicleModel.from_record(row)

    async def get_all(self) -> List[Vehicle]:
        query = vehicles.select()
        async with self.conn.query(query) as cursor:
            res = []
            async for row in cursor:
                res.append(VehicleModel.from_record(row))
                return res

    async def save(self, vehicle):
        pass
