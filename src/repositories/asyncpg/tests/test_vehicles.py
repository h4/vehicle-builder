import pytest
from asyncpgsa import pg

from repositories.asyncpg.vehicles import VehiclePGRepository

HOST = 'localhost'
PORT = 5432
DB_NAME = 'vehicle_builder'
USER = 'postgres'
PASS = 'password'


async def init():
    await pg.init(
        host=HOST,
        port=PORT,
        database=DB_NAME,
        user=USER,
        password=PASS,
        min_size=5,
        max_size=10
    )


@pytest.mark.skip
class TestVehiclesRepository:
    async def test_returns_vehicles_list(self):
        conn = await init()
        repository = VehiclePGRepository(pg)
        vehicles = await repository.get_all()

        assert len(vehicles) > 0

    async def test_returns_vehicle_by_id(self):
        conn = await init()
        repository = VehiclePGRepository(pg)
        vehicle = await repository.find_by_id(1)

        assert vehicle.id == 1

    async def test_returns_none_if_nothing_found(self):
        conn = await init()
        repository = VehiclePGRepository(pg)
        vehicle = await repository.find_by_id(100500)

        assert vehicle is None
