from marshmallow import Schema, fields


class VehicleSchema(Schema):
    id = fields.Int()
    title = fields.String()
    range = fields.Int()
    properties = fields.Nested('VehiclePropertySchema', many=True)


class VehiclePropertySchema(Schema):
    id = fields.Int()
    title = fields.String()
    value = fields.String()
