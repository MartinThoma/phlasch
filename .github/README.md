# Phlasch

A url shortener.

## Support the project

If you liked this project please consider giving it a star! ⭐️

## Goal

Phlasch is a url shortener. It aims to be easy-to-use, flexible and
performant. As a result of this philosophy, it has been designed to be usable
as a program, a docker container or an aiohttp library.

## Requirements

- Python (\>=3.7)

## Installation

1. Make sure your OS has the following prerequisites:

   - build essentials packages (gcc, etc.)
   - postgresql development packages (postgresql-dev, etc.)
   - libffi development packages (libffi-dev, etc.)

2. Upgrade `pip`, `setuptools` and `wheel`.

   ``` bash
   $ pip install --upgrade pip setuptools wheel
   ```

3. Install Phlasch using pip:

   ``` bash
   $ pip install phlasch
   ```

## Configuration

When you install Phlasch you get the following apps:

- DB: to store the links.
- Shortener: to shorten the links.
- Redirector: to redirect to the links.
- Stats: to get some stats about the links.

You can configure each app using its special environment variables, then you
can call its runner to run it.

### DB

DB is the app which stores all the links. it uses the following
environment variables:

- DB_BACKEND

  The database backend to use. e.g. postgresql, sqlite, etc.

  Default: postgresql

  *Note*: Currently only postgresql is supported due to aiopg support.

- DB_DRIVER

  The database driver to use. e.g. psycopg2, pg8000, etc.

  Default: psycopg2

  *Note*: Currently only psycopg2 is supported due to aiopg support.

- DB_USER

  The database user.

  Default: postgres

- DB_PASSWORD

  The database password.

  Default: *nothing*

- DB_HOST

  The database host.

  Default: localhost

- DB_PORT

  The database port.

  Default: 5432

- DB_NAME

  The database name.

  Default: postgres

- DB_URL

  The database url.

  Default: *see note*

  *Note*: If set, it will override all the other DB configurations, otherwise
  it will be set automatically using the other DB configurations.

- DB_ENGINE

  The aiohttp app's engine key.

  Default: phlasch

  If you're not using Phlasch as an aiohttp lib don't mind this, but
  if you are, this is the app key which the database engine is set on after
  creation.

### Shortener

Shortener is the app which shortens all the links. it uses the following
environment variables:

- SHORTENER_BASE

  The characters to use in the shortened url.

  Default: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

  Some people prefer not to use the (O, o, 0), (I, l, 1) or some
  similar-looking characters at all.

  **Warning**: ONCE SET, DO NOT CHANGE THIS! EVER!

- SHORTENER_SHORTEN_URL

  The url on which you can shorten links.

  Default: shortener/shorten

  *Note*: It is set as a slashed url so that it can't be mistaken with a
  shortened url.

- SHORTENER_ORIGIN

  The origin of the shortened url.

  Default: *nothing*

  In case you want to deploy the Redirector app on another host or domain, set
  this to the origin of that host or domain.

  *Note*: If empty, it will use the origin of the Shortener host or domain.
