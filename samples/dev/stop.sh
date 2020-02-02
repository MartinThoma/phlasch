#!/bin/sh
set -o errexit

# remove swarm
docker stack rm phlasch_dev
