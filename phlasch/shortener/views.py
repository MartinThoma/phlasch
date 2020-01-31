from aiohttp import web


async def shorten(request):
    data = await request.json()

    return web.json_response(data)
