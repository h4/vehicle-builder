from marshmallow import Schema, fields

from schemas.fields import UniqueList


class GroupSchema(Schema):
    id = fields.Int()
    title = fields.String()
    is_set = fields.Boolean()
    parent_id = fields.Int()
    children = UniqueList(fields.Int())
    features = UniqueList(fields.Int())


class FeatureSchema(Schema):
    id = fields.Int()
    title = fields.String()
    functions = UniqueList(fields.Int())


class FunctionSchema(Schema):
    id = fields.Int()
    title = fields.String()
