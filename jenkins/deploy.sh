#!/bin/bash
scp -i ~/.ssh/football docker-compose.yaml jenkins@swarm-master:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/football jenkins@swarm-master << EOF
    export DATABASE_URI=${DATABASE_URI} app_version=${app_version} replicas=${replicas}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml football
EOF