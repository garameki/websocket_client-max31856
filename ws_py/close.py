#!/usr/bin/enb python3
#_*_ coding : utf-8 _*_

from frame import Frame

import socket
import select


def close(sock):
	msg = "sayounara"
	frame = Frame.create(Frame.OPCODE_CLOSE,msg)
					
	rrr,www,eee = select.select([],[sock],[],2)
	if www:
		while frame:
			l = sock.send(frame)
			frame = frame[l:]
	else:
		raise UnavailableToSendError

