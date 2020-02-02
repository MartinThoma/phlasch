import pytest

from phlasch.runners import get_runnable
from phlasch.migrators import upgrade, downgrade


@pytest.fixture
def cli(loop, aiohttp_client):
    return loop.run_until_complete(
        aiohttp_client(
            get_runnable('all')
        )
    )


@pytest.fixture(scope='module')
def tables():
    upgrade('db', 'head')
    yield
    downgrade('db', 'base')
