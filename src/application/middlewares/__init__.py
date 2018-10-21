from application.handlers.common_handlers import not_found_handler, internal_error_handler
from application.middlewares.error_handling import error_pages


def setup_middlewares(app):
    error_middleware = error_pages({
        404: not_found_handler,
        500: internal_error_handler,
    })
    app.middlewares.append(error_middleware)
