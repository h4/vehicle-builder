from logging import getLogger

from aiohttp import web


logger = getLogger(__file__)

def error_pages(overrides):
    async def middleware(app, handler):
        async def middleware_handler(request):
            try:
                response = await handler(request)
                override = overrides.get(response.status)
                if override is None:
                    return response
                else:
                    return await override(request, response)
            except web.HTTPException as ex:
                logger.exception(ex)
                override = overrides.get(ex.status)
                if override is None:
                    raise
                else:
                    return await override(request, ex)
            except Exception as ex:
                logger.exception(ex)
                override = overrides.get(500)
                if override is None:
                    raise
                else:
                    return await override(request, ex)
        return middleware_handler
    return middleware
