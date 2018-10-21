from aiohttp import web

from application.middlewares import setup_middlewares
from application.routes import build_routes


def make_app():
    app = web.Application()
    build_routes(app)
    setup_middlewares(app)
    return app
