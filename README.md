# OBP-Docker

Files required to create the images available at Docker Hub
https://hub.docker.com/r/openbankproject/


## Build obp-base

    $ cp Dockerfile.obp-base Dockerfile
    $ docker build -t openbankproject/obp-base .


## Build obp-full

    $ cp Dockerfile.obp-full Dockerfile
    $ docker build -t openbankproject/obp-full .
