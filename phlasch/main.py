from aiohttp.web import Application, run_app
from routes import setup_routes

app = Application()
setup_routes(app)
run_app(app)
