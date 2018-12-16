#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
MIT License

Copyright (c) 2018 garameki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
sys.path.append("/home/pi/src/websocket/client-max31856/ws_py/")
from max31856 import Max31856
import ws_py
from pysocket_client import Pysocket

import time


a = Max31856(0,0)
a.reset()
a.close()

wmax = Pysocket('192.168.3.8',9801)
spi00 = Max31856(0,0)
try:
	while True:
		status = spi00.read()
		if status["FAULT"] != 0:
			spi00.reset()
			count += 1
			print("FAULT")
			if count == 5:
				print("EXTERNAL FAULT{}".format(status["FAULT"]))
				break
		else:
			wmax.send("toC "+str(status["HJ"]*0.0625))
		time.sleep(1)
except BrokenPipeError:
	spi00.close()
	print("\nパイプが切断されました。")
except ConnectionRefusedError:
	spi00.close()
	print("\n接続できませんでした。HOST:{} PORT:{}".format(HOST,PORT))
except KeyboardInterrupt:
	wmax.close()
	spi00.close()
	print("\n切断しました。")
except:
	spi00.close()
	wmax.close()
	raise
	pass
