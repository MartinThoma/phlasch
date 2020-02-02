#!/bin/sh

# no exit on error so that container stops even if test fails
set +o errexit

random=`uuidgen | sed 's/-//g'`

if [ "$1" != "--no-postgres-docker" ]; then
    docker run --rm --name $random -d -p 5433:5432 postgres
    export PHLASCH_DB_PORT=5433
fi

pytest

if [ "$1" != "--no-postgres-docker" ]; then
    docker stop $random
fi
