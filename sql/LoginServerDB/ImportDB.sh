#!/bin/bash

DBHost=$1
DBPort=$2
DBUser=$3
DBPassword=$4

DatabaseName=logindb

DatabaseIndex=0
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

:<<!
DatabaseIndex=1
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

DatabaseIndex=2
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

DatabaseIndex=3
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

DatabaseIndex=4
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

DatabaseIndex=5
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

DatabaseIndex=6
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

DatabaseIndex=7
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

DatabaseIndex=8
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex

DatabaseIndex=9
./ImportTB.sh $DBHost $DBPort $DBUser $DBPassword $DatabaseName $DatabaseIndex
!
