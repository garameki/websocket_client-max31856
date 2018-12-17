#!/usr/bin/env python3
#_*_ coding: utf-8 _*_


import six
import numpy

def mask_data(key,data):
	'''
	4バイトのキーでデータをxorマスクします
	Usage:
		bKey,bMasked = mask_data(aKey,sData)
	Returns:
		(bytes) bKey  : is the key from aKey
		(bytes) bData : is masked data
	Arguments:
		(array) aKey : is key contains 4 byte integer.
		(str) sData  : is letters to be sended
	'''
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

	return key3,maskdata #keyは送りやすい形に直して返す

if __name__ == '__main__':
	#EXAMPLE
	key = [0x37,0xfa,0x21,0x3d]
	data = "Hello"
	keybytes,maskdata = mask_data(key,data)
	print('keybytes =',keybytes)
	print('maskdata =',maskdata)
