class TestVehicleListHandler:
    async def test_smoke(self, aiohttp_client, app):
        client = await aiohttp_client(app)
        resp = await client.get('/vehicles')
        assert resp.status == 200


class TestVehicleItemHandlers:
    async def test_smoke(self, aiohttp_client, app):
        client = await aiohttp_client(app)
        resp = await client.get('/vehicles/1')
        assert resp.status == 200


class TestVehicleConfigurationHandler:
    async def test_smoke(self, aiohttp_client, app):
        client = await aiohttp_client(app)
        resp = await client.get('/vehicles/1/configuration')
        assert resp.status == 200
