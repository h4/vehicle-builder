import pytest
from aiohttp import web

from application import build_routes, setup_middlewares


async def fail_handler(_):
    return 1 / 0


def create_app():
    app = web.Application()
    build_routes(app)
    app.add_routes([web.get('/whoops', fail_handler), ])
    setup_middlewares(app)
    return app


@pytest.fixture
def app():
    return create_app()
