from marshmallow import Schema, fields


class UniqueList(fields.List):
    def _serialize(self, value, attr, obj):
        value = set(value)
        if all(x is None for x in value):
            return []
        return list(value)


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
