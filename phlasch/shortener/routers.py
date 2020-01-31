from aiohttp import web
from phlasch.shortener.settings import SHORTENER_URL
from phlasch.shortener.views import shorten


routes = [
    web.post(f'/{SHORTENER_URL}', shorten, name='shorten'),
]
