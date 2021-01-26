#!/bin/bash

DBHost=$1
DBPort=$2
DBUser=$3
DBPassword=$4
DatabaseName=$5
DatabaseIndex=$6

DBFullName=${DatabaseName}_${DatabaseIndex}
echo "ImportTB.sh $DBFullName"

./Execute.sh  $DBHost $DBPort $DBUser $DBPassword $DBFullName ./config/Rank_DBALLCreateTable.xml

echo ""