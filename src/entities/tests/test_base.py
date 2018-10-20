from dataclasses import dataclass

from entities.base import BaseEntity


def test_entity_may_be_persisted():
    @dataclass
    class Entity(BaseEntity):
        pass

    entity = Entity()
    assert entity.id is None
    entity.id = 42
    assert entity.id == 42
