# OBP-Docker


Files required to create the images available at Docker Hub
https://hub.docker.com/r/openbankproject/


### Build

    $ docker build --no-cache -f api/Dockerfile -t openbankproject/obp-base api




### Run in docker container

    $ docker run -d -p 8080:8080                         \
    -e "OBP_API_HOSTNAME=http://127.0.0.1:8080"          \
    openbankproject/obp-api


# Errors Logging & Debugging

To view the logs of the running OBP API instance:

1. Exec into the running container: `docker exec -it <container-id> /bin/bash`
   this will drop you to a root shell.
2. Tail the jetty log: `tail -f /var/log/supervisor/OBP-API-stdout.log`
3. There are additional logs in `/var/log/supervisor`

To find out your container id run `sudo docker ps`
