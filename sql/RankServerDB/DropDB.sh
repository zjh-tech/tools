#!/bin/bash

DBHost=$1
DBPort=$2
DBUser=$3
DBPassword=$4


mysql=/usr/bin/mysql
$mysql -u$DBUser -h$DBHost -P$DBPort -p$DBPassword < ./sql/DropDB.sql