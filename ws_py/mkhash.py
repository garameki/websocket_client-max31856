#!/usr/bin/enb python3
#_*_ coding : utf-8 _*_


from lib import pt

import six
import hashlib
import base64

def mkhash_16bytes_b64(data):
	#文字列からハッシュを生成しさらにBASE64にエンコードして返す
#	m = hashlib.new('ripemd160') #20桁 #opnsslのライブラリを使う時
	digest = hashlib.md5(six.b(data)).digest() #16桁hashは[RFC6455]より
	key = base64.b64encode(digest)
#	print(data)
	return key

def mkhash_sha1_b64(data):
	#文字列からハッシュを生成しさらにBASE64にエンコードして返す
	m = hashlib.sha1(six.b(data))
	digest = m.digest()
	key = base64.b64encode(digest)
	return key


if __name__=='__main__':

	#文字列を用いる例
	s = "Nobody inspects"
	print(mkhash_b64(s))

	#乱数を用いる例
	from rnd import getRND
	a = getRND(20)
	s=""
	for ele in a:
		s += chr(ele)
	hs = mkhash_b64(s)
	decoded = base64.b64decode(hs)
	print(len(decoded))






