from models.base import BaseModel, db


class Vehicle(BaseModel):
    __tablename__ = 'vehicles'

    title = db.Column(db.String)
    range = db.Column(db.Integer)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._properties = set()

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def add_property(self, prop):
        self._properties.add(prop)


class VehicleProperty(BaseModel):
    __tablename__ = 'vehicle_properties'

    title = db.Column(db.String)
    value = db.Column(db.String)
    vehicle_id = db.Column(None, db.ForeignKey('vehicles.id'))
