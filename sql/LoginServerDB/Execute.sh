#!/bin/bash

DBHost=$1
DBPort=$2
DBUser=$3
DBPassword=$4
DBName=$5
XmlFileName=$6

echo "Execute $DBName  $XmlFileName"

java -jar ../liquibase/liquibase.jar --driver=com.mysql.jdbc.Driver --classpath=../liquibase/lib/mysql-connector-java-5.1.31-bin.jar --changeLogFile=$XmlFileName --url="jdbc:mysql://$DBHost:$DBPort/"$DBName?createDatabaseIfNotExist=true --username=$DBUser --password=$DBPassword  update

