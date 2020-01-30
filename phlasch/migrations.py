from os import path
from alembic.config import main


def makemigrations(app, name):
    main(argv=[
        '-c', path.join(path.dirname(__file__), 'db', 'alembic.ini'),
        'revision',
        '--version-path', path.join(path.dirname(__file__), app, 'versions'),
        '--autogenerate',
        '-m', name,
    ])


def migrate():
    main(argv=[
        '-c', path.join(path.dirname(__file__), 'db', 'alembic.ini'),
        'upgrade',
        'head',
    ])
