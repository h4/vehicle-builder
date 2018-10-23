from marshmallow import fields


class UniqueList(fields.List):
    def _serialize(self, value, attr, obj):
        value = set(value)
        if all(x is None for x in value):
            return []
        return list(value)