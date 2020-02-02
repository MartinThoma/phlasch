#!/bin/sh
set -o errexit

# upgrade database
python -m phlasch upgrade db head

# run
gunicorn phlasch.runners:get_stats_runnable \
    --bind 0.0.0.0:8080 \
    --worker-class aiohttp.GunicornWebWorker
