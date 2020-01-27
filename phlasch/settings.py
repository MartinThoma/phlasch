from utils import get_env_string, get_env_int


# ------------------------------------------------------------------- database

# get database settings from environment variables
DB_USER = get_env_string('PHLASCH_DB_USER', default='postgres')
DB_PASSWORD = get_env_string('PHLASCH_DB_PASSWORD', default='postgres')
DB_HOST = get_env_string('PHLASCH_DB_HOST', default='localhost')
DB_PORT = get_env_int('PHLASCH_DB_PORT', default=5432)
DB_NAME = get_env_string('PHLASCH_DB_NAME', default='postgres')
DB_MIN_SIZE = get_env_int('PHLASCH_DB_MIN_SIZE', default=1)
DB_MAX_SIZE = get_env_int('PHLASCH_DB_MAX_SIZE', default=5)

# either set this directly or it will be set indirectly
DB_URL = get_env_string(
    'PHLASCH_DB_URL',
    default='postgresql://{user}:{password}@{host}:{port}/{database}'.format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )
)
