# This creates a jetty jre8 image containing a local war file.


FROM openjdk:8-jre-alpine

# Add user 
RUN adduser -D obp

# Download jetty
RUN wget -O - https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.4.15.v20190215/jetty-distribution-9.4.15.v20190215.tar.gz | tar zx
RUN mv jetty-distribution-* jetty


# Copy build artifact (.war file) into jetty from local directory.
ADD ./ROOT.war /jetty-distribution-9.4.15.v20190215/webapps/ROOT.war

WORKDIR jetty-distribution-9.4.15.v20190215/
RUN chown -R  obp /jetty-distribution-9.4.15.v20190215

# Switch to the obp user (non root)
USER obp

# Starts jetty
ENTRYPOINT ["java", "-jar", "start.jar"]
