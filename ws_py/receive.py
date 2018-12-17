#!/usr/bin/enb python3
#_*_ coding : utf-8 _*_

import socket
import select
import six
from error import *

def receive(sock):
	rr,ww,ee = select.select([sock],[],[],2)
	if rr:
		data = sock.recv(2048)
		mm = ""
		for ele in data:
			mm += chr(ele)
	#	print(mm,[format(ele,'02x') for ele in data])
		return data
	else:
		raise UnavailableToReceiveDataError


