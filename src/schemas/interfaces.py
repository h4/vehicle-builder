from marshmallow import Schema, fields


class InterfaceSchema(Schema):
    id = fields.Int()
    title = fields.Str()
