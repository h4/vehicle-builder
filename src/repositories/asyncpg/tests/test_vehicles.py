from asyncpgsa.testing import MockPG

from repositories.asyncpg.vehicles import VehiclePGRepository


class TestVehiclesRepository:
    async def test_returns_vehicles_list(self):
        pg = MockPG()
        pg.set_database_results([{"id": 1, "title": "Car", "range": 100}])
        repository = VehiclePGRepository(pg)
        vehicles = await repository.get_all()

        assert len(vehicles) > 0

    async def test_returns_vehicle_by_id(self):
        pg = MockPG()
        pg.set_database_results([{"id": 1, "title": "Car", "range": 100}])
        repository = VehiclePGRepository(pg)
        vehicle = await repository.find_by_id(1)

        assert vehicle.id == 1

    async def test_returns_none_if_nothing_found(self):
        pg = MockPG()
        pg.set_database_results([])
        repository = VehiclePGRepository(pg)
        vehicle = await repository.find_by_id(100500)

        assert vehicle is None
