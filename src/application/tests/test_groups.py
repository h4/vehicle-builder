class TestGroupsHandlers:
    async def test_smoke(self, aiohttp_client, app):
        client = await aiohttp_client(app)
        resp = await client.get('/groups')
        assert resp.status == 200
