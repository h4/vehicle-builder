class TestVehiclesHandlers:
    async def test_smoke(self, aiohttp_client, app):
        client = await aiohttp_client(app)
        resp = await client.get('/vehicles')
        assert resp.status == 200
