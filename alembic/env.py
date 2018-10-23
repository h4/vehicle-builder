from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

import db.tables
import db.base
from settings import Settings

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = db.base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    try:
        settings = Settings()
        url = settings.db_dsn
    except Exception:
        url = config.get_main_option("sqlalchemy.url")

    context.configure(url=url, target_metadata=target_metadata,
                      literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    try:
        settings = Settings()
        connectable = engine_from_config(
            config.get_section(config.config_ini_section),
            url=settings.db_dsn,
            prefix='sqlalchemy.',
            poolclass=pool.NullPool)
    except Exception:
        connectable = engine_from_config(
            config.get_section(config.config_ini_section),
            prefix='sqlalchemy.',
            poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    print('!!! Running in ONLINE mode !!!')
    run_migrations_offline()
else:
    print('!!! Running in ONLINE mode !!!')
    run_migrations_online()
