from aiohttp import web

from application.handlers.common_handlers import root_handler


def create_app():
    app = web.Application()
    app.router.add_get('/', root_handler)
    return app


async def test_root(aiohttp_client):
    app = create_app()
    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    payload = await resp.json()
    assert 'vehicle builder api' in payload['data']
