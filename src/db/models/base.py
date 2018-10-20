import dataclasses


class BaseModel:
    __entity__ = None

    @classmethod
    def from_record(cls, record):
        _cls = cls.__entity__
        fields = set(map(lambda f: f.name, dataclasses.fields(_cls)))
        keys = set(record.keys())
        others = keys - fields

        kwargs = {k: v for k, v in record.items() if k in fields}
        instance = _cls(**kwargs)
        for k in others:
            setattr(instance, k, record[k])

        return instance
