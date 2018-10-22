from models.vehicles import VehicleProperty, Vehicle


async def get_vehicle_by_id(vehicle_id: int):
    query = VehicleProperty.outerjoin(Vehicle, Vehicle.id == vehicle_id).select()
    return await query.gino.load(
        Vehicle.distinct(Vehicle.id).load(add_property=VehicleProperty)
    ).first()


async def get_all_vehicles():
    query = VehicleProperty.outerjoin(Vehicle).select()
    return await query.gino.load(
        Vehicle.distinct(Vehicle.id).load(add_property=VehicleProperty)
    ).all()
