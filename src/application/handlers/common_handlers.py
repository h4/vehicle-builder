from aiohttp import web


async def root_handler(request):
    payload = {
        'data': 'vehicle builder api',
    }
    return web.json_response(payload)
