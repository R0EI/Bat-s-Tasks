#!/bin/bash
API_BASE_URL=$1
TAG=$2
ssh ubuntu@$API_BASE_URL mkdir -p /home/ubuntu/myapp
ssh ubuntu@$API_BASE_URL mkdir -p /home/ubuntu/myapp/templates
ssh ubuntu@$API_BASE_URL mkdir -p /home/ubuntu/myapp/nginx
scp app.py ubuntu@$API_BASE_URL:/home/ubuntu/myapp
scp deploy.sh ubuntu@$API_BASE_URL:/home/ubuntu/myapp
scp prod-docker-compose.yml ubuntu@$API_BASE_URL:/home/ubuntu/myapp
scp Dockerfile.mongo  ubuntu@$API_BASE_URL:/home/ubuntu/myapp
scp Dockerfile.nginx  ubuntu@$API_BASE_URL:/home/ubuntu/myapp
scp nginx/nginx.conf ubuntu@$API_BASE_URL:/home/ubuntu/myapp/nginx
scp init-db.js ubuntu@$API_BASE_URL:/home/ubuntu/myapp              
scp templates/index.html ubuntu@$API_BASE_URL:/home/ubuntu/myapp/templates
scp requirements.txt ubuntu@$API_BASE_URL:/home/ubuntu/myapp
ssh ubuntu@$API_BASE_URL /home/ubuntu/myapp/deploy.sh $TAG