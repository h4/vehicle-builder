"""Add constraints

Revision ID: e087bae23cef
Revises: 0e34d3c4043e
Create Date: 2018-10-23 11:34:04.379333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e087bae23cef'
down_revision = '0e34d3c4043e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_vehicle_configurations__vehicle_feature', 'vehicle_configurations', ['vehicle_id', 'feature_id'])
    op.create_unique_constraint('uq_vehicle_configurations__vehicle_function', 'vehicle_functions', ['vehicle_id', 'function_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_vehicle_configurations__vehicle_function', 'vehicle_functions', type_='unique')
    op.drop_constraint('uq_vehicle_configurations__vehicle_feature', 'vehicle_configurations', type_='unique')
    # ### end Alembic commands ###
