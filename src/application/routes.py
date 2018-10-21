from aiohttp import web
from aiohttp.web_app import Application

from application.handlers.common_handlers import root_handler
from application.handlers.groups import group_list_handler
from application.handlers.vehicles import (
    vehicle_list_handler,
    vehicle_item_handler,
    vehicle_configuration_handler
)


def build_routes(app: Application):
    app.add_routes([
        web.get('/', root_handler),
        web.get('/groups', group_list_handler),
        web.get('/vehicles', vehicle_list_handler),
        web.get(r'/vehicles/{vehicle_id:\d+}', vehicle_item_handler),
        web.get(r'/vehicles/{vehicle_id:\d+}/configuration', vehicle_configuration_handler),
    ])
