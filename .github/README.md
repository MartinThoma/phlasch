# phlasch-server

A url shortener.

## Support the project

If you liked this project please consider giving it a star! ⭐️

## Goal

phlasch-server is a url shortener. It aims to be easy-to-use, flexible and
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

3. Install `phlasch-server` using pip:

   ``` bash
   $ pip install phlasch-server
   ```

## Configuration

When you install phlasch-server you get the following apps:

- shortener: to shorten the links.
- redirector: to redirect to the links.
- stats: to get some stats about the links.
