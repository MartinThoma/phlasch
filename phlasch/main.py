from aiohttp.web import Application, run_app
from configure import setup_app


app = Application()
setup_app(app)
run_app(app)
