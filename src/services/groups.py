from models.base import db
from models.groups import Group


async def get_all_groups():
    SubGroup = Group.alias()

    parents = db.select([SubGroup.parent_id])
    query = Category.load(parent=Parent.on(
        Category.parent_id == Parent.id
    )).where(
        ~Category.id.in_(db.select([Category.alias().parent_id]))
    )

    query = Group.outerjoin(Vehicle).select()
    return await query.gino.load(
        Vehicle.distinct(Vehicle.id).load(add_property=VehicleProperty)
    ).all()