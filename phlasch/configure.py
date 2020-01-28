import aiopg
from settings import DB_URL, DB_ENGINE


# ---------------------------------------------------- database configurations

async def start_db(app):
    engine = await aiopg.sa.create_engine(DB_URL)
    app[DB_ENGINE] = engine


async def clean_db(app):
    engine = app[DB_ENGINE]
    engine.close()
    await engine.wait_closed()


# ----------------------------------------------------- use all configurations

def configure_app(app):
    app.on_startup.append(start_db)
    app.on_cleanup.append(clean_db)
