#!/bin/sh

export MAVEN_OPTS="-Xmx256m -Xms256m -XX:MaxPermSize=128m"

mvn $*
