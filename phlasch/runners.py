from aiohttp.web import Application, run_app
from phlasch.db.configure import configure as configure_db
from phlasch.shortener.configure import configure as configure_shortener


def run():
    app = Application()
    configure_db(app)
    configure_shortener(app)
    run_app(app)
