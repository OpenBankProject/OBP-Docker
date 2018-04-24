FROM openbankproject/obp-base
MAINTAINER OpenBankProject <contact@openbankproject.com>
EXPOSE 8080
# Supervisor
ADD full/supervisor/OBP-API.conf /etc/supervisor/conf.d/
# Clone all repositories
RUN cd /opt/OBP/ && git clone https://github.com/OpenBankProject/OBP-API.git
# API
ADD full/props/OBP-API.default.props /opt/OBP/OBP-API/src/main/resources/props/default.props
ADD full/lift_proto.db.mv.db /opt/OBP/OBP-API/
RUN cd /opt/OBP/OBP-API/ && mvn package -DskipTests
# Run script
ADD api/run_obp /usr/local/sbin/
CMD /usr/local/sbin/run_obp
