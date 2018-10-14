from aiohttp import web


async def root_handler(_):
    payload = [
        {'data': 'vehicle builder api'},
    ]
    return web.json_response(payload)


app = web.Application()
app.add_routes([
    web.get('/', root_handler)
])

web.run_app(app)
