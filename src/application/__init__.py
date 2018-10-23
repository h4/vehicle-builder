from aiohttp import web

from application.middlewares import setup_middlewares
from application.routes import build_routes
from settings import Settings


async def init_db(app):
    from asyncpgsa import pg
    await pg.init(
        host=Settings.db_host,
        port=Settings.db_port,
        database=Settings.db_name,
        user=Settings.db_user,
        password=Settings.db_pass,
        min_size=5,
        max_size=10
    )
    app.on_cleanup.append(close_db)


async def close_db(_):
    from asyncpgsa import pg
    await pg.pool.close()


def make_app():
    app = web.Application()
    build_routes(app)
    setup_middlewares(app)
    app.on_startup.append(init_db)
    return app
