"""Add features tree tables

Revision ID: 7b4d3781b0b0
Revises: 2f3fd38e2543
Create Date: 2018-10-23 05:57:17.516103

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7b4d3781b0b0'
down_revision = '2f3fd38e2543'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('components',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('cad_model', sa.String(length=32), nullable=True),
    sa.Column('sku', sa.String(length=16), nullable=True),
    sa.Column('provider', sa.String(length=16), nullable=True),
    sa.Column('weight', sa.DECIMAL(precision=3), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=2), nullable=True),
    sa.Column('production_status', postgresql.ENUM('UNKNOWN', 'DESIGN', 'PRODUCTION', 'ORDERED', 'IN_STOCK', 'DEPRECATED', name='productionstatus'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_components'))
    )
    op.create_index(op.f('ix_components_production_status'), 'components', ['production_status'], unique=False)
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('path', sqlalchemy_utils.types.ltree.LtreeType(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('is_set', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.CheckConstraint('\n        (is_set = FALSE) OR (parent_id NOTNULL) \n        ', name=op.f('ck_groups__ck_groups__set_has_parent')),
    sa.ForeignKeyConstraint(['parent_id'], ['groups.id'], name=op.f('fk_groups__parent_id__groups'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_groups'))
    )
    op.create_index('ix_features_tree_path_btree', 'groups', ['path'], unique=False, postgresql_using='btree')
    op.create_index('ix_features_tree_path_gist', 'groups', ['path'], unique=False, postgresql_using='gist')
    op.create_index(op.f('ix_groups_parent_id'), 'groups', ['parent_id'], unique=False)
    op.create_table('interfaces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_interfaces'))
    )
    op.create_table('component_properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('property_name', sa.String(length=32), nullable=True),
    sa.Column('value', sa.String(length=32), nullable=True),
    sa.Column('component_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['component_id'], ['components.id'], name=op.f('fk_component_properties__component_id__components'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_component_properties')),
    sa.UniqueConstraint('component_id', 'value', name='uq_component_properties__component_property_name')
    )
    op.create_index(op.f('ix_component_properties_component_id'), 'component_properties', ['component_id'], unique=False)
    op.create_table('features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['groups.id'], name=op.f('fk_features__parent_id__groups'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_features'))
    )
    op.create_index(op.f('ix_features_parent_id'), 'features', ['parent_id'], unique=False)
    op.create_table('functions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('feature_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['feature_id'], ['features.id'], name=op.f('fk_functions__feature_id__features'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_functions'))
    )
    op.create_index(op.f('ix_functions_feature_id'), 'functions', ['feature_id'], unique=False)
    op.create_unique_constraint('uq_vehicle_properties__vehicle_property_name', 'vehicle_properties', ['vehicle_id', 'value'])
    op.drop_constraint('fk_vehicle_properties__vehicle_id__vehicles', 'vehicle_properties', type_='foreignkey')
    op.create_foreign_key(op.f('fk_vehicle_properties__vehicle_id__vehicles'), 'vehicle_properties', 'vehicles', ['vehicle_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_vehicle_properties__vehicle_id__vehicles'), 'vehicle_properties', type_='foreignkey')
    op.create_foreign_key('fk_vehicle_properties__vehicle_id__vehicles', 'vehicle_properties', 'vehicles', ['vehicle_id'], ['id'])
    op.drop_constraint('uq_vehicle_properties__vehicle_property_name', 'vehicle_properties', type_='unique')
    op.drop_index(op.f('ix_functions_feature_id'), table_name='functions')
    op.drop_table('functions')
    op.drop_index(op.f('ix_features_parent_id'), table_name='features')
    op.drop_table('features')
    op.drop_index(op.f('ix_component_properties_component_id'), table_name='component_properties')
    op.drop_table('component_properties')
    op.drop_table('interfaces')
    op.drop_index(op.f('ix_groups_parent_id'), table_name='groups')
    op.drop_index('ix_features_tree_path_gist', table_name='groups')
    op.drop_index('ix_features_tree_path_btree', table_name='groups')
    op.drop_table('groups')
    op.drop_index(op.f('ix_components_production_status'), table_name='components')
    op.drop_table('components')
    old_type = postgresql.ENUM('UNKNOWN', 'DESIGN', 'PRODUCTION', 'ORDERED', 'IN_STOCK', 'DEPRECATED', name='productionstatus')
    old_type.drop(op.get_bind(), checkfirst=False)
    # ### end Alembic commands ###
