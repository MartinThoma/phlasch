# Phlasch

[![build](https://travis-ci.com/bbmokhtari/phlasch.svg?branch=master)](https://travis-ci.com/bbmokhtari/phlasch)
[![pypi](https://img.shields.io/badge/pypi-package-f9d35f.svg)](https://pypi.org/project/phlasch/)
[![docker](https://img.shields.io/badge/docker-image-1388e7.svg)](https://hub.docker.com/r/bbmokhtari/phlasch)

A url shortener.

## Support the project

If you liked this project please consider giving it a star! ⭐️

## Goal

Phlasch is a url shortener. It aims to be easy-to-use, flexible and
performant. As a result of this philosophy, it has been designed to be usable
as a docker image, a program, or an aiohttp library.

## Docker

There are two approaches to deploying Phlasch.

### Unified

An all in one approach, which means the url shortener, redirector and
the stats apps are all deployed as part of one service.

For example:

1. Deploy this `docker-compose.yml` file.

   ``` docker-compose.yml
   version: "3.7"

   services:

     database:
       image: postgres
       restart: always
       environment:
         POSTGRES_PASSWORD: postgres

     server:
       image: bbmokhtari/phlasch
       restart: always
       ports:
         - 8080:8080
       environment:
         PHLASCH_DB_HOST: database
         PHLASCH_DB_PASSWORD: postgres
   ```

2. Navigate to http://localhost:8080/api/doc to see what APIs are available.

   ![image](https://raw.githubusercontent.com/bbmokhtari/phlasch/master/docs/_static/swagger_all.png)

### Divided

A separated approach, which means the url shortener, redirector and
the stats apps are all deployed separately as different services.

For example:

1. Deploy this `docker-compose.yml` file.

   ``` docker-compose.yml
   version: "3.7"

   services:

     database:
       image: postgres
       restart: always
       environment:
         POSTGRES_PASSWORD: postgres

     shortener:
       image: bbmokhtari/phlasch
       command: ./start-shortener.sh
       restart: always
       ports:
         - 8080:8080
       environment:
         PHLASCH_DB_HOST: database
         PHLASCH_DB_PASSWORD: postgres
         PHLASCH_SHORTENER_ORIGIN: http://localhost:9090

     redirector:
       image: bbmokhtari/phlasch
       command: ./start-redirector.sh
       restart: always
       ports:
         - 9090:8080
       environment:
         PHLASCH_DB_HOST: database
         PHLASCH_DB_PASSWORD: postgres

     stats:
       image: bbmokhtari/phlasch
       command: ./start-stats.sh
       restart: always
       ports:
         - 7070:8080
       environment:
         PHLASCH_DB_HOST: database
         PHLASCH_DB_PASSWORD: postgres
         PHLASCH_STATS_ORIGIN: http://localhost:9090
   ```

2. Navigate to http://localhost:8080/api/doc to see what APIs are available.

   ![image](https://raw.githubusercontent.com/bbmokhtari/phlasch/master/docs/_static/swagger_shortener.png)

3. Navigate to http://localhost:9090/api/doc to see what APIs are available.

   ![image](https://raw.githubusercontent.com/bbmokhtari/phlasch/master/docs/_static/swagger_redirector.png)

4. Navigate to http://localhost:7070/api/doc to see what APIs are available.

   ![image](https://raw.githubusercontent.com/bbmokhtari/phlasch/master/docs/_static/swagger_stats.png)

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

  If you are not using Phlasch as an aiohttp lib don't mind this, but
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

- **PHLASCH_STATS_ORIGIN**

  The origin of the shortened url.

  Default: *nothing*

  In case the Redirector app is deployed on another host or domain, set
  this to the origin of that host or domain.

  *Note*: If empty, it will use the origin of the Stats host or domain.

## CLI: Command Line Interface

When the configurations are in place, the command line interface can be used
effectively.

To see what is available, run the cli with the `-h` option:

``` bash
python -m phlasch -h
```

It will print something like this:

```
usage: phlasch [-h] {run,history,revision,upgrade,downgrade} ...

A url shortener.

optional arguments:
  -h, --help            show this help message and exit

Action:
  The action to take.

  {run,history,revision,upgrade,downgrade}
    run                 Run app.
    history             Log revisions.
    revision            Make revision.
    upgrade             Upgrade to revision.
    downgrade           Downgrade to revision.
```

As seen above, the command line interface provides some actions which can be
taken.

### Migrators

Phlasch database migrations are being tracked using revisions. Each time the
database schema is changed in any app by Phlasch developers a revision is
created in that app. Revisions represent the points in which the database
schema was changed, as a result we can upgrade or downgrade to any revision
at any time.

#### Upgrade

Each time Phlasch is installed or is updated, it is a good idea to upgrade
to the latest revision (or head) for each database-using app, in the current
case: only the DB app.

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

#### History

To log the revisions of the DB app, run:

``` bash
python -m phlasch history db
```

It will print something like this:

```
Rev: bfd35ebcbeb5 (head)
Parent: <base>
Path: /app/phlasch/db/migrations/versions/bfd35ebcbeb5_added_link_table.py

    added link table
    
    Revision ID: bfd35ebcbeb5
    Revises: 
    Create Date: 2020-01-30 21:29:35.727874+00:00

```

#### Downgrade

If we encounter any weird database situations after an upgrade we can always
downgrade to the previous revisions.

To downgrade the DB app to the none revision (base), run:

``` bash
python -m phlasch downgrade db base
```

It will print something like this:

```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade bfd35ebcbeb5 -> , added link table
```

**WARNING**: SETTING DOWNGRADE TO BASE WILL DELETE EVERYTHING AND DROP ALL TABLES!

#### Revision

If you are contributing to Phlasch and happen to change database schemas,
you can create a revision for that change.

To create a revision for the DB app, run:

``` bash
python -m phlasch revision db "some message"
```

It will print something like this:

```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.ddl.postgresql] ...
  Generating /app/phlasch/db/migrations/versions/1fb7a742b953_some_message.py ...  done
```

### Runners

After migrating to the desired revision, either a single app or all apps can
be run.

#### Aiohttp

Apps can be run using the aiohttp server.

To run all apps, run:

``` bash
python -m phlasch run all
```

It will print something like this:

```
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```

Now you can navigate to http://localhost:8080/api/doc to see what
APIs are available!

![image](https://raw.githubusercontent.com/bbmokhtari/phlasch/master/docs/_static/swagger_all.png)

To run a single app, run:

``` bash
python -m phlasch run ${app_name}
```

It will print something like this:

```
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```

#### Gunicorn

Apps can be run using the Gunicorn wsgi server.

To run all apps, run:

``` bash
gunicorn phlasch.runners:get_all_runnable \
    --bind 0.0.0.0:8080 \
    --worker-class aiohttp.GunicornWebWorker
```

It will print something like this:

```
[2020-02-03 03:59:38 +0330] [80163] [INFO] Starting gunicorn 20.0.4
[2020-02-03 03:59:38 +0330] [80163] [INFO] Listening at: http://0.0.0.0:8080 (80163)
[2020-02-03 03:59:38 +0330] [80163] [INFO] Using worker: aiohttp.GunicornWebWorker
[2020-02-03 03:59:38 +0330] [80166] [INFO] Booting worker with pid: 80166
```

Now you can navigate to http://localhost:8080/api/doc to see what
APIs are available!

![image](https://raw.githubusercontent.com/bbmokhtari/phlasch/master/docs/_static/swagger_all.png)

To run a single app, run:

``` bash
gunicorn phlasch.runners:get_${app_name}_runnable \
    --bind 0.0.0.0:8080 \
    --worker-class aiohttp.GunicornWebWorker
```

It will print something like this:

```
[2020-02-03 04:01:13 +0330] [80251] [INFO] Starting gunicorn 20.0.4
[2020-02-03 04:01:13 +0330] [80251] [INFO] Listening at: http://0.0.0.0:8080 (80251)
[2020-02-03 04:01:13 +0330] [80251] [INFO] Using worker: aiohttp.GunicornWebWorker
[2020-02-03 04:01:13 +0330] [80254] [INFO] Booting worker with pid: 80254
```

## Aiohttp library

If the configurations are set, Phlasch can also be used as an aiohttp library.

1. If you are using [alembic](https://alembic.sqlalchemy.org) as your
   migration tool add the following lines to `alembic.ini`.

   ``` .ini
   [db]
   script_location = %(location_of_phlasch_package)s/db/migrations
   version_locations = %(location_of_phlasch_package)s/db/migrations/versions
   ```

   If not, simply run the [upgrade](#upgrade) command described above in the
   migrators sections.

2. Configure your app using the configure functions provided by the apps.

   ``` python
   from phlasch.db.configure import configure as configure_db
   from phlasch.shortener.configure import configure as configure_shortener
   from phlasch.stats.configure import configure as configure_stats
   from phlasch.redirector.configure import configure as configure_redirector
   
   # your app
   app = Application()
   ...
   # please keep this configure order intact
   configure_db(app)
   configure_shortener(app)
   configure_stats(app)
   configure_redirector(app)
   ...
   ```
