# OBP-Docker

Files required to create the images available at Docker Hub
https://hub.docker.com/r/openbankproject/


## Build obp-base

    $ docker build --no-cache -f Dockerfile.obp-base -t openbankproject/obp-base .


## Build obp-full

    $ docker build --no-cache -f Dockerfile.obp-full -t openbankproject/obp-full .


## Run obp-full in docker container

    docker run -d -p 8080-8082:8080-8082                           \
    -e "ADVERTISED_HOST=localhost"                                 \
    -e "OBP_API_HOSTNAME=http://127.0.0.1:8080"                    \
    -e "OBP_BASE_URL_API_EXPLORER=http://localhost:8082"           \
    -e "OBP_BASE_URL_SOCIAL_FINANCE=http://localhost:8081"         \
    -e "OBP_WEBUI_API_EXPLORER_URL=http://localhost:8082"          \
    openbankproject/obp-full


## Build obp-full-kafka

    $ docker build --no-cache -f Dockerfile.obp-full-kafka -t openbankproject/obp-full-kafka .


## Run obp-full-kafka in docker container 

    docker run -d -p 8080-8082:8080-8082 -p 9092:9092 -p 2181:2181 \
    -e "ADVERTISED_HOST=localhost"                                 \
    -e "OBP_API_HOSTNAME=http://127.0.0.1:8080"                    \
    -e "OBP_BASE_URL_API_EXPLORER=http://localhost:8082"           \
    -e "OBP_BASE_URL_SOCIAL_FINANCE=http://localhost:8081"         \
    -e "OBP_WEBUI_API_EXPLORER_URL=http://localhost:8082"          \
    openbankproject/obp-full-kafka
