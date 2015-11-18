#!/bin/sh

export MAVEN_OPTS="-Xmx384m -Xms384m -XX:MaxPermSize=256m"

mvn $*
