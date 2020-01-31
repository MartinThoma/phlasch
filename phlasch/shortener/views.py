from aiohttp import web
from phlasch.shortener.validators import validate_url


async def shorten(request, data):
    # validate data
    address = data.get('address')
    if not address:
        return web.json_response({
            'address': 'this field can not be blank.',
        }, status=400)
    if not validate_url(address):
        return web.json_response({
            'address': 'this field must be a valid url.',
        }, status=400)

    return web.json_response(data)
