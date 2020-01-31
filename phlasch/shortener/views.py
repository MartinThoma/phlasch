from aiohttp import web
from phlasch.db.settings import SA_ENGINE
from phlasch.core.queries import create_link, update_link_shortcut
from phlasch.shortener.validators import validate_url
from phlasch.shortener.utils import convert_base


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

    # insert into database
    engine = request.app[SA_ENGINE]
    async with engine.acquire() as conn:
        row = await create_link(conn, address)
        pk = row['id']
        shortcut = convert_base(pk)
        await update_link_shortcut(conn, pk, shortcut)

        return web.json_response({
            'shortcut': shortcut,
        })
