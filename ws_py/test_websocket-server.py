#!/usr/bin/env python3

#_*_coding : utf-8_*_

import os
import six
import numpy

from lib import pt
OPCODES = (0x0,0x1,0x2,0x8,0x9,0xa)

fin = 1
rsv1 = 0
rsv2 = 0
rsv3 = 0
opcode = 0x1
mask = 1

data = "0123456789ABCDEF";pt('data = "0123456789ABCDEF"',data)
data += "0123456789ABCDEF";pt('data += "0123456789ABCDEF"',data)
data += "0123456789ABCDEF";pt('data += "0123456789ABCDEF"',data)
data += "0123456789ABCDEF";pt('data += "0123456789ABCDEF"',data)

#from _core.py 269	data = frame.format()
#to   _abnf.py 211	def format(self)
if any(x not in (0,1) for x in [fin,rsv1,rsv2,rsv3]):
	stop()
if opcode not in OPCODES:
	stop()
length = len(data)
if length >= 4*4*4*4*4*4*4*4:
	stop()

byte = fin *   0x80;pt("byte = fin",byte)
byte += rsv1 * 0x40;pt("byte += rsv1 * 0x40000000",byte)
byte += rsv2 * 0x20;pt("byte += rsv2 * 0x20000000",byte)
byte += rsv3 * 0x10;pt("byte += rsv3 * 0x10000000",byte)
byte += opcode;pt("byte += opcode",byte)
frame_header = chr(byte);pt("frame_header = chr(byte)",frame_header)
if length < 127:
	frame_header += chr(mask * 0x80 + length);pt('frame_header += chr(mask * 0x80 + length)',frame_header)
	frame_header = six.b(frame_header);pt('frame_header = six.b(frame_header)',frame_header)
elif length < 2^16:
	frame_header += chr(mask * 0x80 + 126);pt('frame_header += chr(mask * 0x80 + 126)',frame_header)
	frame_header = six.b(frame_header);pt('frame_header = six.b(frame_header)',frame_header)
	frame_header += struct.pack("!H",length);pt('frame_header += struct.pack("!H",length)',frame_header)
else:
	frame_header += chr(mask * 0x80 + 127);pt('frame_header += chr(mask * 0x80 + 127)',frame_header)
	frame_header = six.b(frame_header);pt('frame_header = six.b(frame_header)',frame_header)
	frame_header += struct.pack("!Q",length);pt('frame_header += struct.pack("!Q",length)',frame_header)

mask_key = os.urandom(4);pt('mask_key = os.urandom(4)',mask_key)

#from _abnf.py 242
#to   _abnf.py 244	_get_masked(mask_key)

if isinstance(mask_key, six.text_type):
	mask_key = six.b(mask_key);pt('mask_key = six.b(mask_key)',mask_key)

if isinstance(data, six.text_type):
	data = six.b(data);pt('data = six.b(data)',data)

origlen = len(data);pt('origlen = len(data)',origlen)
_mask_key = mask_key[3] << 24 | mask_key[2] << 16 | mask_key[1] << 8 | mask_key[0];pt('_mask_key = mask_key[3] << 24 | mask_key[2] << 16 | mask_key[1] << 8 | mask_key[0]',_mask_key)

data += bytes(" " * (4 -(len(data) % 4)),"us-ascii");pt('data += bytes(" " * (4 -(len(data) % 4)),"us-ascii")',data)
a = numpy.frombuffer(data, dtype="uint32");pt('a = numpy.frombuffer(data, dtype="uint32")',a)
masked = numpy.bitwise_xor(a, [_mask_key]);pt('masked = numpy.bitwise_xor(a, [_mask_key])',masked)
masked = masked.astype("uint32");pt('masked = masked.astype("uint32")',masked)
if len(data) > origlen:
	ret = masked.tobytes()[:origlen];pt('ret = masked.tobytes()[:origlen]',ret)
else:
	ret = masked.tobytes();pt('ret = masked.tobytes()',ret)

#return _abnf.py 242
ret = frame_header + ret;pt('ret = frame_header + ret',ret)

#return _core.py 269	data = frame.format()
data_core = ret;pt('data_core = ret',data_core)
length = len(data_core);pt('length = len(data_core)',length)

#from _core.py 271	trace("send: " + repr(data_core))
#to   _logging.py 72	def trace(msg)

#from _logging.py 74	_logger.debug(msg)
#to   _logging.py 24	_logger = logging.getLogger('websocket')

import logging

_logger = logging.getLogger('test')
from logging import NullHandler
_logger.addHandler(NullHandler)

#return _logging.py 74
_logger.debug("send: " + repr(data_core))

#return _core.py 271

while data_core:

#from _core.py 275	l = self._send(data)
#to   _core.py 444		def _send(self, data):

#from _core.py 445	return send(self.sock, data)
#to   _socket.py 109	def send(sock, data)

	if isinstance(data_core,six.text_type):
		data_core = data_core.encode("utf-8");pt('data_core = data_core.encode("utf-8")',data_core)

if not sock:
	stop()

#from _socket.py 117	return sock.send(data)

# _core.py 186 def connect(self, url, **options):これが、WebSocket.connect(...)
# _core.py 219 self.sock, addrs = connect(url, self.sock_opt, proxy_info(**options), options.pop('socket',None))
# _http.py  24 import socket
# _http.py 103 def connect(url, options, proxy, socket):
#		addrinfo_list, need_tunnel, auth = _get_addrinfo_list(...)
# _http.py 137 def _get_addrinfo_list(hostname, port, is_secure, proxy):
#		addrinfo_list = socket.getaddrinfo(phost, pport, 0, socket.SOC_STREAM, socket.SOL_TCP)
# _http.py 157 def _open_socket(addrinfo_list, sockopt, timeout)
# 		for addrinfo in addrinfo_list:
#		family, socktype, proto = addrinfo[:3]
#		sock = socket.socket(family, socktype, proto)
#		sock.timeout(timeout)
#		address = addrinfo[4]
#		sock.connect(address)
#		return sock
# _http.py 161 sock = socket.socket(family, socktype, proto)
#to   _




