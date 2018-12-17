#!/usr/bin/enb python3
#_*_ coding : utf-8 _*_

from lib import pt
from handshake import handshake
from mkhash import mkhash_16bytes_b64 as mkhash_b64
from send import send
from receive import receive
from close import close
from error import *

from rnd import getRND

import time
import socket
import select
import six

import sys

class Pysocket:
	def __init__(self,host,port):
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			self.sock.connect((host,port))
			handshake(self.sock)

		except BrokenPipeError:
			print("\nパイプが切断されました。")
		except ConnectionRefusedError:
			print("\n接続できませんでした。HOST:{} PORT:{}".format(HOST,PORT))
		except KeyboardInterrupt:
			close(self.sock)
			receive(self.sock)
			print("\n切断しました。")
		except:
			raise


	def send(self,data):
		send(self.sock,data)
		response = receive(self.sock)
		return response

	def close(self):
		close(self.sock)


if __name__ == '__main__':
	host = "192.168.3.6"
	port = 9801
	wmax = Pysocket(host,port)
	data = "toC 26.55"
	wmax.send(data)
	wmax.close()

