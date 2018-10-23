import ujson
from aiohttp.helpers import sentinel
from aiohttp.web_response import Response


def json_response(data=sentinel, *, text=None, body=None, status=200,
                  reason=None, headers=None, content_type='application/json'):
    if data is not sentinel:
        if text or body:
            raise ValueError(
                "only one of data, text, or body should be specified"
            )
        else:
            text = ujson.dumps(data, indent=2)
    return Response(text=text, status=status, reason=reason,
                    headers=headers, content_type=content_type)
