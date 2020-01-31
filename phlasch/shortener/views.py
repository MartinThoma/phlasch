from json.decoder import JSONDecodeError
from aiohttp import web
from phlasch.db.settings import SA_ENGINE
from phlasch.core.queries import create_link, update_link_shortcut
from phlasch.shortener.validators import validate_url
from phlasch.shortener.utils import convert_base
from phlasch.shortener.settings import SHORTENER_ORIGIN


async def shorten(request):
    # retrieve json data
    try:
        data = await request.json()
    except JSONDecodeError:
        return web.json_response({
            'non_field_errors': 'json data must be provided.',
        }, status=400)

    # validate address
    address = data.get('address')
    if not address:
        return web.json_response({
            'address': 'this field can not be blank.',
        }, status=400)
    if not validate_url(address):
        return web.json_response({
            'address': 'this field must be a valid url.',
        }, status=400)

    # insert into database
    engine = request.app[SA_ENGINE]
    async with engine.acquire() as conn:
        row = await create_link(conn, address)
        pk = row['id']
        shortcut = convert_base(pk)
        await update_link_shortcut(conn, pk, shortcut)

    # calculate shortener origin
    if SHORTENER_ORIGIN:
        origin = SHORTENER_ORIGIN
    else:
        origin = f'{request.scheme}://{request.host}'

    # return shortened url
    return web.json_response({
        'url': f'{origin}/{shortcut}',
        'origin': origin,
        'shortcut': shortcut,
    })
