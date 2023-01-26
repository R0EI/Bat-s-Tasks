#!/bin/bash
TAG=$1
export TAG
cd myapp
aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-3.amazonaws.com
docker rmi $(docker images -aq)
docker-compose -f prod-docker-compose.yml build --no-cache
docker-compose -f prod-docker-compose.yml up -d