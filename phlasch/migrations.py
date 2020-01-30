from os import path
from alembic.config import main


def makemigrations(name):
    main(argv=[
        '-c',
        path.join(path.dirname(__file__), 'core', 'alembic.ini'),
        'revision',
        '--autogenerate',
        '-m', name,
    ])


def migrate():
    main(argv=[
        '-c',
        path.join(path.dirname(__file__), 'core', 'alembic.ini'),
        'upgrade',
        'head',
    ])
