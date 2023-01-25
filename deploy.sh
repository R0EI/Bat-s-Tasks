#!/bin/bash
cd myapp
docker rmi $(docker images -aq)
docker-compose build --no-cache
docker-compose up -d