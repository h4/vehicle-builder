"""Fix is_frosen vehicle_functions property

Revision ID: 0e34d3c4043e
Revises: a4b8a6228245
Create Date: 2018-10-23 11:29:30.060010

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0e34d3c4043e'
down_revision = 'a4b8a6228245'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicle_functions', 'is_frozen',
                    existing_type=sa.BOOLEAN(),
                    server_default=sa.text('FALSE'),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicle_functions', 'is_frozen',
                    existing_type=sa.BOOLEAN(),
                    nullable=True)
    # ### end Alembic commands ###
