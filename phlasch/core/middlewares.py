from json.decoder import JSONDecodeError
from aiohttp import web


@web.middleware
async def jsoner(request, handler):
    if request.method not in ('POST', 'PUT'):
        response = await handler(request)
        return response

    try:
        data = await request.json()
        response = await handler(request, data)
        return response
    except JSONDecodeError:
        return web.json_response({
            'non_field_errors': 'json data must be provided.',
        }, status=400)
