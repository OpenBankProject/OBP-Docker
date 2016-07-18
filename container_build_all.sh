docker build --no-cache -f Dockerfile.obp-base       -t openbankproject/obp-base .
docker build --no-cache -f Dockerfile.obp-full       -t openbankproject/obp-full .
docker build --no-cache -f Dockerfile.obp-full-kafka -t openbankproject/obp-full-kafka .
