from aiohttp import web

from application import make_app

app = make_app()

web.run_app(app)
