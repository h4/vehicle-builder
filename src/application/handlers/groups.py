from aiohttp.web_response import json_response

from models.groups import Group, Feature, Function
from schemas.groups import GroupSchema, FeatureSchema, FunctionSchema

group_schema = GroupSchema()
feature_schema = FeatureSchema()
function_schema = FunctionSchema()


async def group_list_handler(request):
    groups = await Group.fetch_many()
    features_ids = [idx for g in groups for idx in g.features]
    features = await Feature.fetch_by_ids(features_ids)
    functions_ids = [idx for f in features for idx in f.functions]
    functions = await Function.fetch_by_ids(functions_ids)

    result = {
        'data': group_schema.dump(groups, many=True).data,
        'included': {
            'features': feature_schema.dump(features, many=True).data,
            'functions': function_schema.dump(functions, many=True).data,
        }
    }
    return json_response(result)
