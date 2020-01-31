from aiohttp.web import Application, run_app
from phlasch.db.configure import configure as configure_db
from phlasch.shortener.configure import configure as configure_shortener
from phlasch.redirector.configure import configure as configure_redirector


def run():
    app = Application()
    configure_db(app)
    configure_shortener(app)
    configure_redirector(app)
    run_app(app)
