#!/usr/bin/enb python3
#_*_ coding : utf-8 _*_

from error import *
from frame import Frame

import socket
import select

def send(sock,msg):
	length = len(msg)
	frame = Frame.create(Frame.OPCODE_TEXT,msg)
					
	rrr,www,eee = select.select([],[sock],[],2)
	if www:
		while frame:
			l = sock.send(frame)
			frame = frame[l:]
		return length
	else:
		raise UnavailableToSendError

