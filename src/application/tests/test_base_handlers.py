from aiohttp import web


async def test_root(aiohttp_client, app):
    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    payload = await resp.json()
    assert 'vehicle builder api' in payload['data']


async def test_not_found_handler(aiohttp_client, app):
    client = await aiohttp_client(app)
    resp = await client.get('/not_exists')
    assert resp.status == 404
    assert 'application/json' in resp.headers['content-type']
    payload = await resp.json()
    assert 'error' in payload


async def test_server_error_handler(aiohttp_client, app):
    client = await aiohttp_client(app)
    resp = await client.get('/whoops')
    assert resp.status == 500
    assert 'application/json' in resp.headers['content-type']
    payload = await resp.json()
    assert 'error' in payload
