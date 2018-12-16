#!/usr/bin/env python3
#_*_ coding: utf-8 _*_


import six
import numpy

def mask_data(key,data):
	length = len(data);
	data += "0" * (4 - length % 4);
	data = six.b(data);
	data = numpy.frombuffer(data,dtype="uint32");

	key2 = key[3] << 24 | key[2] << 16 | key[1] << 8 | key[0];

	maskdata = numpy.bitwise_xor(data,[key2]).astype("uint32");
	maskdata = maskdata.tobytes()[:length];

	key3 = ""
	for ele in key:
		key3 += chr(ele)
	key3 = six.b(key3);

	return key3,maskdata

if __name__ == '__main__':

	from lib import pt

	key = [0x37,0xfa,0x21,0x3d];pt('	key = [0x37,0xfa,0x21,0x3d]',	key)
	data = "Hello";pt('	data = "Hello"',	data)
	keybytes,maskdata = mask_data(key,data)
	print("Return:")
	pt('	keybytes =',	keybytes)
	pt('	maskdata =',	maskdata)
