FROM maven:3-jdk-8
MAINTAINER OpenBankProject <contact@openbankproject.com>
ENV LANG=C.UTF-8 LANGUAGE=C LC_ALL=C.UTF-8 TERM=linux
# Base directory
RUN mkdir --parents /opt/OBP
# Supervisor and debug/monitoring utils
RUN \
 apt-get update &&\
 apt-get upgrade --yes &&\
 apt-get install --yes supervisor bash curl git vim htop telnet net-tools && \
 apt-get clean
# Supervisor
ADD base/supervisor/etc_default_supervisor /etc/default/supervisor
# ElasticSearch
ENV ES_PKG_NAME elasticsearch-2.3.3
RUN \
  cd / && \
  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz && \
  tar xvzf $ES_PKG_NAME.tar.gz && \
  rm -f $ES_PKG_NAME.tar.gz && \
  mv /$ES_PKG_NAME /opt/OBP/elasticsearch
