#!/bin/bash

aa=$(nc -v -z -w 1 192.168.3.8 9801)
if [[ $aa=~success ]]; then
	echo "success"
else
	echo "failure"
fi

