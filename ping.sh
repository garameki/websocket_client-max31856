#!/bin/bash

aa=$(2>&1  nc -v -z -w 1 192.168.3.8 9801)
echo $aa
if [[ $aa =~ port.+succeeded ]]; then
	echo "success"
else
	echo "failure"
fi

