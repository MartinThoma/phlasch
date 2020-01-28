from settings import DB_URL


def setup_app(app):
    app['phlasch_db_url'] = DB_URL
