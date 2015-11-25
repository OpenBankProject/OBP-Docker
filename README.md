# OBP-Docker

Files required to create the images available at Docker Hub
https://hub.docker.com/r/openbankproject/


## Build obp-base

    $ docker build -f Dockerfile.obp-base -t openbankproject/obp-base .


## Build obp-full

    $ docker build -f Dockerfile.obp-full -t openbankproject/obp-full .


## Build obp-full-kafka

    $ docker build -f Dockerfile.obp-full-kafka -t openbankproject/obp-full-kafka .
