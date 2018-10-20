import sqlalchemy as sa

metadata = sa.MetaData()

vehicles = sa.Table('vehicles', metadata,
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('title', sa.String(32)),
                    sa.Column('range', sa.Integer))
