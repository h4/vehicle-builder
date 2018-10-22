from aiohttp.web_response import json_response, Response

from schemas.vehicles import VehicleSchema
from services import vehicles as vehicles_service


async def vehicle_list_handler(request):
    async with request.app['conn'].acquire():
        vehicle = await vehicles_service.get_all_vehicles()
        data = VehicleSchema()
        result = data.dumps(vehicle, many=True)
    return Response(text=result.data)


async def vehicle_item_handler(request):
    async with request.app['conn'].acquire():
        vehicle_id = int(request.match_info.get('vehicle_id'))
        vehicle = await vehicles_service.get_vehicle_by_id(vehicle_id)
        data = VehicleSchema()
        result = data.dumps(vehicle)
    return Response(text=result.data)


async def vehicle_configuration_handler(request):
    vehicle_id = int(request.match_info.get('vehicle_id'))
    payload = {
        'vehicle_id': vehicle_id,
        'error': 'Not implemented yet',
    }
    return json_response(payload)
