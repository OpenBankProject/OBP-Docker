FROM openbankproject/obp-full
MAINTAINER OpenBankProject <contact@openbankproject.com>
EXPOSE 2181 9092
# Kafka
ENV SCALA_VERSION 2.11
ENV KAFKA_VERSION 0.11.0.2
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"
RUN wget -q http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz \
         -O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \
    tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \
    rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
ADD kafka/scripts/start-kafka.sh /usr/local/sbin/start-kafka.sh
# Supervisor
ADD kafka/supervisor/*.conf /etc/supervisor/conf.d/
# API
ADD kafka/props/OBP-API.default.props /opt/OBP/OBP-API/src/main/resources/props/default.props
# Clean, build and cache dependencies
RUN cd /opt/OBP/OBP-API/ && mvn package -DskipTests
