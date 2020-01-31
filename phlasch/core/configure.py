from phlasch.core.middlewares import jsoner


# ------------------------------------------------------------------------ app

# configure everything
def configure(app):
    app.middlewares.append(jsoner)
