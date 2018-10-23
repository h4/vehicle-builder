from marshmallow import Schema, fields

from schemas.fields import UniqueList


class ConfigurationSchema(Schema):
    id = fields.Int()
    vehicle_id = fields.Int()
    feature_id = fields.Int()


class VehicleFunctionsSchema(Schema):
    id = fields.Int()
    vehicle_id = fields.Int()
    function_id = fields.Int()
    features = UniqueList(fields.Int())
    connections = UniqueList(fields.Int())
    is_frozen = fields.Bool()
