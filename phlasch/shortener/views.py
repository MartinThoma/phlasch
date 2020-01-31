from aiohttp import web


async def shorten(request, data):
    return web.json_response(data)
