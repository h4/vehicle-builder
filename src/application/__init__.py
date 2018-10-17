from aiohttp import web

from application.routes import build_routes


def make_app():
    app = web.Application()
    build_routes(app)
    return app
