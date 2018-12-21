# OBP-Docker

Files required to create the images available at Docker Hub
https://hub.docker.com/r/openbankproject/


## obp-base

### Build

    $ docker build --no-cache -f Dockerfile.obp-base -t openbankproject/obp-base .



## obp-api

### Build

    $ docker build --no-cache -f Dockerfile.obp-api -t openbankproject/obp-api .


### Run in docker container

    $ docker run -d -p 8080:8080                         \
    -e "OBP_API_HOSTNAME=http://127.0.0.1:8080"          \
    openbankproject/obp-api



## obp-full

### Build

    $ docker build --no-cache -f Dockerfile.obp-full -t openbankproject/obp-full .


### Run in docker container

    $ docker run -d -p 8080-8082:8080-8082                         \
    -e "OBP_API_HOSTNAME=http://127.0.0.1:8080"                    \
    -e "OBP_BASE_URL_API_EXPLORER=http://localhost:8082"           \
    -e "OBP_BASE_URL_SOCIAL_FINANCE=http://localhost:8081"         \
    -e "OBP_WEBUI_API_EXPLORER_URL=http://localhost:8082"          \
    openbankproject/obp-full



## obp-full-kafka

### Build

    $ docker build --no-cache -f Dockerfile.obp-full-kafka -t openbankproject/obp-full-kafka .


### Run in docker container 

    $ docker run -d -p 8080-8082:8080-8082 -p 9092:9092 -p 2181:2181 \
    -e "ADVERTISED_HOST=localhost"                                   \
    -e "OBP_API_HOSTNAME=http://127.0.0.1:8080"                      \
    -e "OBP_BASE_URL_API_EXPLORER=http://localhost:8082"             \
    -e "OBP_BASE_URL_SOCIAL_FINANCE=http://localhost:8081"           \
    -e "OBP_WEBUI_API_EXPLORER_URL=http://localhost:8082"            \
    openbankproject/obp-full-kafka

# Docker Compose

Docker compose is used to orchestrate the services. The docker images for api, apiexplorer, sofi and postgres are built separately. Using docker compose the services can be run together.

To run the services using docker compose, run the following commands.

    $ cd compose
    $ docker-compose up

# Viewing Errors & Logging

To view the logs of the running OBP API instance:

1. Exec into the running container: `docker exec -it <container-id> /bin/bash`
   this will drop you to a root shell.
2. Tail the jetty log: `tail -f  OBP-API-stdout.log`
3. There are additional logs in `/var/log/supervisor`

To find out your container id run `sudo docker ps`
