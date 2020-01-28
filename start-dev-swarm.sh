#!/bin/sh

# build phlasch-server
docker build -t phlasch-server .

# pull postgres
docker pull postgres

# create database volume
mkdir -p volumes/database

# deploy swarm
docker stack deploy -c docker-compose.yml phlasch
