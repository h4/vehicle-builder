from db.models.base import BaseModel
from entities.vehicle import Vehicle


class VehicleModel(BaseModel):
    __entity__ = Vehicle
