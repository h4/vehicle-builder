import pytest


@pytest.mark.skip
class TestVehicleListHandler:
    async def test_smoke(self, aiohttp_client, app, pg):
        client = await aiohttp_client(app)
        resp = await client.get('/vehicles')
        assert resp.status == 200


@pytest.mark.skip
class TestVehicleItemHandlers:
    async def test_smoke(self, aiohttp_client, app, pg):
        client = await aiohttp_client(app)
        resp = await client.get('/vehicles/1')
        assert resp.status == 200


@pytest.mark.skip
class TestVehicleConfigurationHandler:
    async def test_smoke(self, aiohttp_client, app, pg):
        client = await aiohttp_client(app)
        resp = await client.get('/vehicles/1/configuration')
        assert resp.status == 200
