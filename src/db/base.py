import sqlalchemy as sa

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s__%(column_0_name)s',
    'ck': 'ck_%(table_name)s__%(constraint_name)s',
    'fk': 'fk_%(table_name)s__%(column_0_name)s__%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}
metadata = sa.MetaData(naming_convention=naming_convention)
