from aiohttp.web_response import json_response


async def vehicle_list_handler(request):
    payload = {
        'error': 'Not implemented yet',
    }
    return json_response(payload)
