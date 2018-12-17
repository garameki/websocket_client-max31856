#!/bin/bash

sleep 20
aa=$(2>&1 nc -v -z -w 1 192.168.3.8 9801)
if [[ $aa = ~success ]]; then
	/usr/bin/python3.5 /home/pi/src/websocket/client-max31856/websocket-client-max31856-9801-2.py
	echo python3 websocket-client-max31856-9801.py
else
	echo "port 192.168.3.8 9801 didn't pong"
	exit 1
fi

