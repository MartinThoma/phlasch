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

1. Make sure the OS has the following prerequisites:

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

When Phlasch is installed, the following apps are made available:

- DB: to store the links.
- Shortener: to shorten the links.
- Redirector: to redirect to the links.
- Stats: to get the stats of the links.

Each app can be configured using its own special environment variables.

### DB

DB is the app which stores the links.
it uses the following environment variables:

- **PHLASCH_DB_BACKEND**

  The database backend to use. e.g. postgresql, sqlite, etc.

  Default: postgresql

  *Note*: Currently only postgresql is supported due to aiopg support.

- **PHLASCH_DB_DRIVER**

  The database driver to use. e.g. psycopg2, pg8000, etc.

  Default: psycopg2

  *Note*: Currently only psycopg2 is supported due to aiopg support.

- **PHLASCH_DB_USER**

  The database user.

  Default: postgres

- **PHLASCH_DB_PASSWORD**

  The database password.

  Default: *nothing*

- **PHLASCH_DB_HOST**

  The database host.

  Default: localhost

- **PHLASCH_DB_PORT**

  The database port.

  Default: 5432

- **PHLASCH_DB_NAME**

  The database name.

  Default: postgres

- **PHLASCH_DB_URL**

  The database url.

  Default: *see note*

  *Note*: If set, it will override all the other DB configurations, otherwise
  it will be set automatically using the other DB configurations.

- **PHLASCH_DB_ENGINE**

  The aiohttp app's engine key.

  Default: phlasch

  If you're not using Phlasch as an aiohttp lib don't mind this, but
  if you are, this is the app key which the database engine is set on after
  creation.

### Shortener

Shortener is the app which shortens the links.
it uses the following environment variables:

- **PHLASCH_SHORTENER_BASE**

  The characters to use in the shortened url.

  Default: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

  Some people prefer not to use the (O, o, 0), (I, l, 1) or some
  similar-looking characters at all.

  **Warning**: ONCE SET, DO NOT CHANGE THIS! EVER!

- **PHLASCH_SHORTENER_SHORTEN_URL**

  The url on which the users can shorten links.

  Default: shortener/shorten

  *Note*: It is set as a slashed url so that it can't be mistaken with a
  shortened url.

- **PHLASCH_SHORTENER_ORIGIN**

  The origin of the shortened url.

  Default: *nothing*

  In case the Redirector app is deployed on another host or domain, set
  this to the origin of that host or domain.

  *Note*: If empty, it will use the origin of the Shortener host or domain.

### Redirector

Redirector is the app which redirects to the links. it uses no
environment variables.

### Stats

Stats is the app which is used to get the stats of the links.
it uses the following environment variables:

- **PHLASCH_STATS_LIST_URL**

  The url on which the users can list the stats of all links.

  Default: stats/list

  *Note*: It is set as a slashed url so that it can't be mistaken with a
  shortened url.

- **PHLASCH_STATS_RETRIEVE_URL**

  The url on which the users can retrieve the stats of a link.

  Default: stats/retrieve

  *Note*: It is set as a slashed url so that it can't be mistaken with a
  shortened url.

## CLI: Command Line Interface

When the configurations are in place, the command line interface can be used
effectively.

To see what is available, run the cli with the `-h` option:

``` bash
python -m phlasch -h
```

It will print something like this:

```
usage: phlasch [-h] {run,revision,upgrade,downgrade} ...

A url shortener.

optional arguments:
  -h, --help            show this help message and exit

Action:
  The action to take.

  {run,revision,upgrade,downgrade}
    run                 Run app.
    revision            Make revision.
    upgrade             Upgrade to revision.
    downgrade           Downgrade to revision.
```

As seen above, the command line interface provides some actions which can be
taken.

### Revisions

Phlasch database migrations are being tracked using revisions. Each time the
database schema is changed in any app by Phlasch developers a revision is
created in that app. Revisions represent the points in which the database
schema was changed, as a result we can upgrade or downgrade to any revision
at any time.

So each time Phlasch is installed or is updated, it is a good idea to upgrade
to the latest revision (or head) for each database-using app, in the current
case: only the DB app.

**Upgrade**

To upgrade the DB app to the latest revision (head), run:

``` bash
python -m phlasch upgrade db head
```

It will print something like this:

```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> bfd35ebcbeb5, added link table
```
