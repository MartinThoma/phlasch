#!/bin/sh

current_dir=`dirname $0`
parent_dir=`dirname $current_dir`
root_dir=`dirname $parent_dir`

# build phlasch-server
docker build -t phlasch-server:dev $root_dir

# pull postgres
docker pull postgres

# create database volume
mkdir -p $current_dir/volumes/database

# deploy swarm
docker stack deploy -c $current_dir/docker-compose.yml phlasch_dev
