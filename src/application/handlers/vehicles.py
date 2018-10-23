from aiohttp.web_response import json_response, Response

from models.vehicles import Vehicle, VehicleProperty
from schemas.vehicles import VehicleSchema, VehiclePropertySchema

vehicle_schema = VehicleSchema()
vehicle_property_schema = VehiclePropertySchema()


async def vehicle_list_handler(request):
    vehicles = await Vehicle.fetch_many()
    property_idx = [idx for v in vehicles for idx in v.properties]
    properties = await VehicleProperty.fetch_by_ids(property_idx)

    result = {
        'data': vehicle_schema.dump(vehicles, many=True).data,
        'included': vehicle_property_schema.dump(properties, many=True).data
    }
    return json_response(result)


async def vehicle_item_handler(request):
    pk = int(request.match_info.get('vehicle_id'))
    vehicle = await Vehicle.fetch_by_id(pk)
    properties = await VehicleProperty.fetch_by_ids(vehicle.properties)

    result = {
        'data': vehicle_schema.dump(vehicle).data,
        'included': vehicle_property_schema.dump(properties, many=True).data
    }
    return json_response(result)


async def vehicle_configuration_handler(request):
    vehicle_id = int(request.match_info.get('vehicle_id'))
    payload = {
        'vehicle_id': vehicle_id,
        'error': 'Not implemented yet',
    }
    return json_response(payload)
