from models.base import db
from models.vehicles import Vehicle, VehicleProperty  # noqa
from models.groups import Group, Function, Feature  # noqa


async def migrate():
    await db.gino.create_all()
