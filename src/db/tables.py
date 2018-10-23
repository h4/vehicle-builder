import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlalchemy.dialects import postgresql

from db.enums import ProductionStatus
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
    sa.Column('vehicle_id',
              sa.ForeignKey('vehicles.id', ondelete='CASCADE'),
              nullable=False),

    sa.UniqueConstraint('vehicle_id', 'value',
                        name='uq_vehicle_properties__vehicle_property_name')
)

components = sa.Table(
    'components', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(32)),
    sa.Column('cad_model', sa.String(32)),
    sa.Column('sku', sa.String(16)),
    sa.Column('provider', sa.String(16)),
    sa.Column('weight', sa.DECIMAL(precision=3)),
    sa.Column('price', sa.DECIMAL(precision=2)),
    sa.Column('production_status', postgresql.ENUM(ProductionStatus),
              nullable=False, default=ProductionStatus.UNKNOWN, index=True),
)

component_properties = sa.Table(
    'component_properties', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('property_name', sa.String(32)),
    sa.Column('value', sa.String(32)),
    sa.Column('component_id',
              sa.ForeignKey('components.id', ondelete='CASCADE'),
              nullable=False, index=True),

    sa.UniqueConstraint('component_id', 'value',
                        name='uq_component_properties__component_property_name')
)

groups = sa.Table(
    'groups', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(32)),
    sa.Column('parent_id', sa.ForeignKey('groups.id', ondelete='CASCADE'),
              nullable=True, index=True),
    sa.Column('path', sau.LtreeType(), nullable=True,
              default=None, server_default=sa.text('NULL')),
    sa.Column('is_set', sa.Boolean(),
              nullable=False, default=False, server_default=sa.text('FALSE')),

    sa.Index('ix_features_tree_path_gist', 'path', postgresql_using='gist'),
    sa.Index('ix_features_tree_path_btree', 'path', postgresql_using='btree'),

    sa.CheckConstraint(
        """
        (is_set = FALSE) OR (parent_id NOTNULL) 
        """,
        name='ck_groups__set_has_parent'
    )
)

features = sa.Table(
    'features', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(32)),
    sa.Column('parent_id', sa.ForeignKey('groups.id', ondelete='CASCADE'),
              nullable=False, index=True),
)

functions = sa.Table(
    'functions', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(32)),
    sa.Column('feature_id', sa.ForeignKey('features.id', ondelete='CASCADE'),
              nullable=False, index=True),
)

interfaces = sa.Table(
    'interfaces', metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(32)),
)
