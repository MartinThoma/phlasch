from aiohttp.web import Application, run_app
from phlasch.core.configure import configure as configure_core


app = Application()
configure_core(app)
run_app(app)
