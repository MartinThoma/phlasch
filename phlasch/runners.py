from aiohttp.web import Application, run_app
from aiohttp_swagger import setup_swagger
from phlasch.db.configure import configure as configure_db
from phlasch.shortener.configure import configure as configure_shortener
from phlasch.stats.configure import configure as configure_stats
from phlasch.redirector.configure import configure as configure_redirector


def run(app_name):
    app = Application()
    configure_db(app)
    if app_name in ('all', 'shortener',):
        configure_shortener(app)
    if app_name in ('all', 'stats',):
        configure_stats(app)
    if app_name in ('all', 'redirector',):
        configure_redirector(app)
    setup_swagger(app)
    run_app(app)
