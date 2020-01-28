from aiohttp.web import Application, run_app
from configure import configure_app


app = Application()
configure_app(app)
run_app(app)
