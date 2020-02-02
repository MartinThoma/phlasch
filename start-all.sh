#!/bin/sh
set -o errexit

# migrate database
python -m phlasch migrate db

# run
gunicorn phlasch.runners:get_all_runnable \
    --bind 0.0.0.0:8080 \
    --worker-class aiohttp.GunicornWebWorker
