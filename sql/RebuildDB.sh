#!/bin/bash

DBHost=127.0.0.1
DBPort=3306
DBUser=root
DBPassword=123456


SERVERLIST='LoginServerDB CenterServerDB RankServerDB GameServerDB'

CurPath=`pwd`

for Serv in $SERVERLIST
do 
    cd $CurPath/$Serv	
	./DropDB.sh    $DBHost $DBPort $DBUser $DBPassword
    ./CreateDB.sh  $DBHost $DBPort $DBUser $DBPassword	
    ./ImportDB.sh  $DBHost $DBPort $DBUser $DBPassword
	echo ""
done

