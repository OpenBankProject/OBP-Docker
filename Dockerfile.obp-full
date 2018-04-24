FROM openbankproject/obp-base
MAINTAINER OpenBankProject <contact@openbankproject.com>
EXPOSE 8080 8081 8082
# Supervisor
ADD full/supervisor/*.conf /etc/supervisor/conf.d/
# Clone all repositories
RUN cd /opt/OBP/ && git clone https://github.com/OpenBankProject/OBP-API.git
RUN cd /opt/OBP/ && git clone https://github.com/OpenBankProject/Social-Finance.git
RUN cd /opt/OBP/ && git clone https://github.com/OpenBankProject/API-Explorer.git
# API
ADD full/props/OBP-API.default.props /opt/OBP/OBP-API/src/main/resources/props/default.props
ADD full/lift_proto.db.mv.db /opt/OBP/OBP-API/
RUN cd /opt/OBP/OBP-API/ && mvn package -DskipTests
# Social Finance
ADD full/props/Social-Finance.default.props /opt/OBP/Social-Finance/src/main/resources/props/default.props
RUN cd /opt/OBP/Social-Finance/ && mvn package -DskipTests
# API Explorer
ADD full/props/API-Explorer.default.props /opt/OBP/API-Explorer/src/main/resources/props/default.props
RUN cd /opt/OBP/API-Explorer/ && mvn package -DskipTests
# Run script
ADD full/run_obp /usr/local/sbin/
CMD /usr/local/sbin/run_obp
