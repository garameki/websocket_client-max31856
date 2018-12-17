#!/usr/bin/enb python3
#_*_ coding : utf-8 _*_

from lib import pt
from rnd import getRND
from mask import mask_data
from mkhash import mkhash_16bytes_b64 as mkhash_b64
from error import *

from frame import Frame

import time

import base64
import hashlib

import numpy
import six
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

