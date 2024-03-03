#!/bin/bash

# Ubuntu or KaliLinux

chmod -R 777 ./

apt-get update
apt-get install -y docker.io

mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose version

docker swarm init
docker node update --label-add='name=linux-1' $(docker node ls -q)

docker-compose up -d

rm -rf docker-compose-linux-x86_64
rm -rf dockerimages
rm -rf initDocker.sh

rm -rf start.sh

