#!/bin/bash
docker rmi $(docker images -aq)
docker pull 644435390668.dkr.ecr.eu-west-2.amazonaws.com/yuval-klechevsky-repo:${New_tag}
docker compose build --no-cache
docker compose up -d