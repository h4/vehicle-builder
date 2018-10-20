import sqlalchemy as sa
from sqlalchemy.orm import mapper

from entities.vehicle import Vehicle

metadata = sa.MetaData()

vehicles = sa.Table('vehicles', metadata,
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('title', sa.String(32)),
                    sa.Column('range', sa.Integer))


VehicleMap = mapper(Vehicle, vehicles)
