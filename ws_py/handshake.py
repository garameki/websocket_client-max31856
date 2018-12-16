#!/usr/bin/enb python3
#_*_ coding : utf-8 _*_

from lib import pt
from mkhash import mkhash_sha1_b64
from mkhash import mkhash_16bytes_b64 as mkhash_b64
from rnd import getRND
from receive import receive
from error import *

import select
import re
import six

def handshake(sock):
	rnds = getRND(20)
	phrase = ""
	for ele in rnds:
		phrase += chr(ele)
	key_b64 = mkhash_b64(phrase)
	rrr,www,eee = select.select([],[sock],[],2)
	if www:
		sock.send(b'GET / HTTP/1.1\r\n')
		sock.send(b'Host: 192.168.3.6\r\n')
		sock.send(b'Upgrade: websocket\r\n')
		sock.send(b'Connection: Upgrade\r\n')
		sock.send(b'Sec-WebSocket-Key: ' + key_b64 + b'\r\n')
		sock.send(b'Origin: http://example.com\r\n')
		sock.send(b'Sec-WebSocket-Protocol: chat, superchat\r\n')
		sock.send(b'Sec-WebSocket-Version: 13\r\n\r\n')
		response = receive(sock);pt('		response = receive(sock)',		response)
		_recog(response,key_b64)
	else:
		raise UnavailableToSendHandShakeError

def _recog(response,key_client):
	moji = ""
	for ele in response:
		moji += chr(ele)
	hash_server  = re.search('Sec-WebSocket-Accept:\s([^\s]+)',moji).group(1).strip()
	moji = ""
	for ele in key_client:
		moji += chr(ele)
	temp =  mkhash_sha1_b64(moji + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11")
	hash_client = ""
	for ele in temp:
		hash_client += chr(ele)
	if hash_server != hash_client:
		raise HashNotMatchError
	
