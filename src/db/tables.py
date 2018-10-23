import sqlalchemy as sa

from .base import metadata

vehicles = sa.Table(
    'vehicles', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(32)),
    sa.Column('range', sa.Integer)
)

vehicle_properties = sa.Table(
    'vehicle_properties', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('property_name', sa.String(32)),
    sa.Column('value', sa.String(32)),
    sa.Column('vehicle_id', sa.ForeignKey('vehicles.id'), nullable=False)
)
