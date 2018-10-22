from aiohttp import web

from application.middlewares import setup_middlewares
from application.routes import build_routes
from models.base import db
from models.utils import migrate


async def init_db(app):
    conn = await db.set_bind('postgresql://postgres:password@localhost/vehicle_builder')
    app['conn'] = conn
    async with app['conn'].acquire():
        await migrate()


async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()


def make_app():
    app = web.Application()
    build_routes(app)
    setup_middlewares(app)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    return app
