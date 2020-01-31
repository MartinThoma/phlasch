from os import path
from alembic.config import main


def makemigrations(app, name):
    main(argv=[
        '-c', path.join(path.dirname(__file__), 'alembic.ini'),
        '--name', app,
        'revision', '-m', name,
        '--autogenerate'
    ])


def migrate(app):
    main(argv=[
        '-c', path.join(path.dirname(__file__), 'alembic.ini'),
        '--name', app,
        'upgrade', 'head',
    ])
