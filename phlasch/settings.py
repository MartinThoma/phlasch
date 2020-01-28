from utils import get_env_string, get_env_int


# ------------------------------------------------------------------- database

# get database settings from environment variables
DB_BACKEND = get_env_string('PHLASCH_DB_BACKEND', default='postgresql')
DB_DRIVER = get_env_string('PHLASCH_DB_DRIVER', default='')
DB_USER = get_env_string('PHLASCH_DB_USER', default='postgres')
DB_PASSWORD = get_env_string('PHLASCH_DB_PASSWORD', default='')
DB_HOST = get_env_string('PHLASCH_DB_HOST', default='localhost')
DB_PORT = get_env_int('PHLASCH_DB_PORT', default=5432)
DB_NAME = get_env_string('PHLASCH_DB_NAME', default='postgres')
DB_MIN_SIZE = get_env_int('PHLASCH_DB_MIN_SIZE', default=1)
DB_MAX_SIZE = get_env_int('PHLASCH_DB_MAX_SIZE', default=5)

# calculate intermediary database settings
DB_DIALECT = '{backend}{plus}{driver}'.format(
    backend=DB_BACKEND,
    plus='+' if DB_DRIVER else '',
    driver=DB_DRIVER,
)
DB_AUTH = '{user}{column}{password}'.format(
    user=DB_USER,
    column=':' if DB_PASSWORD else '',
    password=DB_PASSWORD,
)
DB_ADDRESS = '{host}{colon}{port}'.format(
    host=DB_HOST,
    column=':' if DB_PORT else '',
    port=DB_PORT,
)

# either set this directly or it will be set indirectly
DB_URL = get_env_string(
    'PHLASCH_DB_URL',
    default='{dialect}://{auth}@{address}/{database}'.format(
        dialect=DB_DIALECT,
        auth=DB_AUTH,
        address=DB_ADDRESS,
        database=DB_NAME,
    )
)
