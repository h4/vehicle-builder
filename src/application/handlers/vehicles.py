from aiohttp.web_response import json_response, Response

from models.components import Component
from models.configurations import VehicleFunctions, VehicleConnections
from models.groups import Feature, Function
from models.interfaces import Interface
from models.vehicles import Vehicle, VehicleProperty
from schemas.components import ComponentSchema
from schemas.configurations import VehicleFunctionsSchema
from schemas.groups import FeatureSchema, FunctionSchema
from schemas.interfaces import InterfaceSchema
from schemas.vehicles import VehicleSchema, VehiclePropertySchema

component_schema = ComponentSchema()
feature_schema = FeatureSchema()
function_schema = FunctionSchema()
interface_schema = InterfaceSchema()
vehicle_schema = VehicleSchema()
vehicle_property_schema = VehiclePropertySchema()
vehicle_functions_schema = VehicleFunctionsSchema(exclude=('vehicle_id',))


async def vehicle_list_handler(request):
    vehicles = await Vehicle.fetch_many()
    property_idx = [idx for v in vehicles for idx in v.properties]
    properties = await VehicleProperty.fetch_by_ids(property_idx)

    result = {
        'data': vehicle_schema.dump(vehicles, many=True).data,
        'included': {
            'properties': vehicle_property_schema.dump(properties, many=True).data,
        }
    }
    return json_response(result)


async def vehicle_item_handler(request):
    pk = int(request.match_info.get('vehicle_id'))
    vehicle = await Vehicle.fetch_one(pk)
    properties = await VehicleProperty.fetch_by_ids(vehicle.properties)

    result = {
        'data': vehicle_schema.dump(vehicle).data,
        'included': vehicle_property_schema.dump(properties, many=True).data
    }
    return json_response(result)


async def vehicle_configuration_handler(request):
    pk = int(request.match_info.get('vehicle_id'))
    vehicle_functions = await VehicleFunctions.fetch_many(
        filter_by={'vehicle_id': pk})
    features_ids = [idx for item in vehicle_functions for idx in item.features]
    connections_ids = [idx for item in vehicle_functions
                       for idx in item.connections]
    function_ids = [v.function_id for v in vehicle_functions]

    connections = await VehicleConnections.fetch_by_ids(connections_ids)
    features = await Feature.fetch_by_ids(features_ids)
    functions = await Function.fetch_by_ids(function_ids)

    components_ids = [c.component_id for c in connections]
    interfaces_ids = [c.interface_id for c in connections]

    components = await Component.fetch_by_ids(components_ids)
    interfaces = await Interface.fetch_by_ids(interfaces_ids)

    result = {
        'data': vehicle_functions_schema.dump(
            vehicle_functions, many=True).data,
        'included': {
            'features': feature_schema.dump(features, many=True).data,
            'functions': function_schema.dump(functions, many=True).data,
            'components': component_schema.dump(components, many=True).data,
            'interfaces': interface_schema.dump(interfaces, many=True).data,
        }
    }
    return json_response(result)
