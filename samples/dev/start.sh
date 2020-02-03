#!/bin/sh
set -o errexit

# list of useful directories
current_dir=`dirname $0`
parent_dir=`dirname $current_dir`
root_dir=`dirname $parent_dir`

# build phlasch
docker build -t phlasch:dev $root_dir

# pull postgres
docker pull postgres

# deploy swarm
docker stack deploy -c $current_dir/docker-compose.yml phlasch_dev
