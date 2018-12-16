#!/bin/bash

if [ -e max31856.py ]; then
	if [ -f max31856.py ]; then
		mv max31856.py max31856.py.1
	fi
fi
cp ~/src/spi/max31856/max31856.py max31856.py
