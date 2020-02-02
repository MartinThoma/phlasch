#!/bin/sh
gunicorn phlasch.runners:get_shortener_runnable --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornWebWorker
