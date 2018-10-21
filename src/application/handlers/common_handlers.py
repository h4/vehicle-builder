from aiohttp import web


async def root_handler(request):
    payload = {
        'data': 'vehicle builder api',
    }
    return web.json_response(payload)


async def not_found_handler(request, exc):
    payload = {
        'error': 'Not Found',
    }
    return web.json_response(payload, status=exc.status)


async def internal_error_handler(request, exc):
    payload = {
        'error': 'Internal Error',
    }
    return web.json_response(payload, status=exc.status)
