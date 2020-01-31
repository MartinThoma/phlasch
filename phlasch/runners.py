from aiohttp.web import Application, run_app
from phlasch.db.configure import configure as configure_db
from phlasch.core.configure import configure as configure_core
from phlasch.shortener.configure import configure as configure_shortener


def run():
    app = Application()
    configure_db(app)
    configure_core(app)
    configure_shortener(app)
    run_app(app)
