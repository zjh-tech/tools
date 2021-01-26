#!/bin/bash

DBHost=$1
DBPort=$2
DBUser=$3
DBPassword=$4

DatabaseName=rankdb

DatabaseIndex=0
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex


