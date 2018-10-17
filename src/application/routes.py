from aiohttp import web
from aiohttp.web_app import Application

from application.handlers.common_handlers import root_handler


def build_routes(app: Application):
    app.add_routes([
        web.get('/', root_handler)
    ])
