from aiohttp.web import Application, run_app
from phlasch.db.configure import configure as configure_db


def run():
    app = Application()
    configure_db(app)
    run_app(app)
