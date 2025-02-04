# This repository is deprecated and archived. #

# OBP-Docker


Files required to create the images available at Docker Hub
https://hub.docker.com/r/openbankproject/


### Build

    $ docker build --no-cache -f Dockerfile.obp-base -t openbankproject/obp-base .




### Run in docker container

    $ docker run -d -p 8080:8080                         \
    -e "OBP_API_HOSTNAME=http://127.0.0.1:8080"          \
    openbankproject/obp-base
    
    
### Overwriting configuration parameters by environment variables

Any configuration in api/default.props can also be overwritten at container creation by
passing an environment variable. 

Use the configured prefix (default: OBP_), capitalize all letters and convert all '.' to '_'
.
E.g.:  'db.url' -> 'OBP_DB_URL'

# Errors Logging & Debugging

To view the logs of the running OBP API instance:

1. Exec into the running container: `docker exec -it <container-id> /bin/bash`
   this will drop you to a root shell.
2. Tail the jetty log: `tail -f /var/log/supervisor/OBP-API-stdout.log`
3. There are additional logs in `/var/log/supervisor`

To find out your container id run `sudo docker ps`
