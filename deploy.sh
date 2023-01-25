#!/bin/bash
docker rmi $(docker images -aq)
docker pull 644435390668.dkr.ecr.eu-west-3.amazonaws.com/roei:1.1.1
docker-compose build --no-cache
docker-compose up -d
