#!/bin/bash
TAG=$1
export TAG
cd myapp
docker rmi $(docker images -aq)
docker-compose -f prod-docker-compose.yml build --no-cache
docker-compose -f prod-docker-compose.yml up -d