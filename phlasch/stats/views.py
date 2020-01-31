from aiohttp import web
from phlasch.db.settings import DB_ENGINE
from phlasch.db.queries import list_links, retrieve_link


async def stats_list(request):
    # list from database
    engine = request.app[DB_ENGINE]
    async with engine.acquire() as conn:
        rows = await list_links(conn)

    # return stats list
    return web.json_response(rows)


async def stats_retrieve(request):
    # validate shortcut
    shortcut = request.match_info.get('shortcut')
    if not shortcut:
        return web.json_response({
            'shortcut': 'this field is required.',
        }, status=400)

    # retrieve from database
    engine = request.app[DB_ENGINE]
    async with engine.acquire() as conn:
        row = await retrieve_link(conn, shortcut)

    # not found
    if not row:
        return web.json_response({
            'shortcut': 'this field does not exist.',
        }, status=404)

    # return stats retrieve
    return web.json_response(row)
