#!/usr/bin/enb python3
#_*_ coding : utf-8 _*_

from lib import pt
from rnd import getRND
from mask import mask_data
from mkhash import mkhash_16bytes_b64 as mkhash_b64
import error

import base64
import hashlib

import numpy
import six
import socket
import select


class Frame:
	OPCODES = (0x0,0x1,0x2,0x8,0x9,0xa)
	OPCODE_TEXT = 0x1
	OPCODE_CLOSE = 0x8

	@classmethod
	def create(sock,opcode,msg):
		fin = 1
		rsv1 = 0
		rsv2 = 0
		rsv3 = 0
		mask = 1

		if any(x not in (0,1) for x in [fin,rsv1,rsv2,rsv3]):
			raise FirstFrameBitError
		if opcode not in Frame.OPCODES:
			raise OpcodeError
		length = len(msg)
		if length > 125 :
			raise TooLongMessaeError

		byte = fin *   0x80;pt("byte = fin",byte)
		byte += rsv1 * 0x40;pt("byte += rsv1 * 0x40000000",byte)
		byte += rsv2 * 0x20;pt("byte += rsv2 * 0x20000000",byte)
		byte += rsv3 * 0x10;pt("byte += rsv3 * 0x10000000",byte)
		byte += opcode;pt("byte += opcode",byte)
		frame_header = chr(byte);pt("frame_header = chr(byte)",frame_header)
		frame_header += chr(mask * 0x80 + length);pt('frame_header += chr(mask * 0x80 + length)',frame_header)
		frame_header_bytes = six.b(frame_header);pt('frame_header_bytes = six.b(frame_header)',frame_header_bytes)

		mask_key = getRND(4);pt('mask_key = rnds = getRND(4)',mask_key)
		mask_key_bytes,data_masked_bytes = mask_data(mask_key,msg)

		frame = frame_header_bytes + mask_key_bytes + data_masked_bytes;pt('frame = frame_header_bytes + mask_key_bytes + data_masked_bytes',frame)
		return frame
