#!/bin/bash

#pp=$(pwd)ルートになってしまうので使えません
pp=/home/pi/src/websocket/client-max31856
sleep 5
aa=$(2>&1 nc -v -z -w 1 192.168.3.8 9801)
if [[ $aa =~ succeeded ]]; then
	echo "start"
	/usr/bin/python3.5 $pp/websocket-client-max31856-9801-2.py
else
	echo "stop"
	echo "port 192.168.3.8 9801 didn't pong"
	systemctl stop websocket-client-max31856-9801
	exit 1
fi

