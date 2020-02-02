from aiohttp.web import Application, run_app
from aiohttp_swagger import setup_swagger
from phlasch.db.configure import configure as configure_db
from phlasch.shortener.configure import configure as configure_shortener
from phlasch.stats.configure import configure as configure_stats
from phlasch.redirector.configure import configure as configure_redirector


# --------------------------------------- runnables and runners for event loop

def get_runnable(app_name):
    app = Application()
    configure_db(app)
    if app_name in ('all', 'shortener',):
        configure_shortener(app)
    if app_name in ('all', 'stats',):
        configure_stats(app)
    if app_name in ('all', 'redirector',):
        configure_redirector(app)
    setup_swagger(app)
    return app


def run(app_name):
    run_app(get_runnable(app_name))


# ----------------------------------------- app factories for aiohttp gunicorn

async def get_all_runnable():
    return get_runnable('all')


async def get_shortener_runnable():
    return get_runnable('shortener')


async def get_stats_runnable():
    return get_runnable('stats')


async def get_redirector_runnable():
    return get_runnable('redirector')
