from application.response import json_response


async def root_handler(request):
    payload = {
        'data': 'vehicle builder api',
    }
    return json_response(payload)


async def not_found_handler(request, exc):
    payload = {
        'error': 'Not Found',
    }
    return json_response(payload, status=exc.status)


async def internal_error_handler(request, exc):
    payload = {
        'error': 'Internal Error',
    }
    return json_response(payload, status=getattr(exc, 'status', 500))
