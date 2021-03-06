"""Update constraints

Revision ID: 2f3fd38e2543
Revises: 9593d51df39f
Create Date: 2018-10-23 02:10:51.289599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f3fd38e2543'
down_revision = '9593d51df39f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicle_properties', 'vehicle_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicle_properties', 'vehicle_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
