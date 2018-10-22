from marshmallow import Schema, fields


class GroupSchema(Schema):
    id = fields.Int()
    title = fields.String()
    is_set = fields.Boolean()
    subgroups = fields.Nested('GroupSchema', many=True)
    features = fields.Nested('FeatureSchema', many=True)


class FeatureSchema(Schema):
    id = fields.Int()
    title = fields.String()
    functions = fields.Nested('FunctionSchema', many=True)


class FunctionSchema(Schema):
    id = fields.Int()
    title = fields.String()
