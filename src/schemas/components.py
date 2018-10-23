from marshmallow import Schema, fields

from schemas.fields import UniqueList


class ComponentSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    cad_model = fields.Str()
    sku = fields.Str()
    provider = fields.Str()
    weight = fields.Int()
    price = fields.Int()
    properties = UniqueList(fields.Int())
