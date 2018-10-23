from marshmallow import Schema, fields


class VehicleSchema(Schema):
    id = fields.Int()
    title = fields.String()
    range = fields.Int()
    properties = fields.List(fields.Int())


class VehiclePropertySchema(Schema):
    id = fields.Int()
    property_name = fields.String(dump_to='name')
    value = fields.String()
