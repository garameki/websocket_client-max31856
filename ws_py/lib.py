#!/usr/bin/env python3
#_*_coding : utf-8_*_

import os
import six
import numpy
import hashlib
hl = type(hashlib.new('ripemd160'))


def pt(string,variable=None):
	if False:
		if variable is None:
			pass	
		elif  type(variable) is str:
			print("{} {} {}".format(string,type(variable),variable))
		elif type(variable) is bytes:
			print("{} {} {}".format(string,type(variable),[format(ele,'01x') for ele in variable]))
		elif type(variable) is numpy.ndarray:
			print("{} {} {}".format(string,type(variable),[format(ele,'08x') for ele in variable]))
		elif type(variable) is hl:
			print("{} {} {}".format(string,type(variable),variable))
		elif  type(variable) is int:
			try:
				print("{} {} {}".format(string,variable__class__.__name__,[format(ele,'01x') for ele in variable]))
			except: 
				print("{} {} {}".format(string,type(variable),format(variable,'01x')))

		else:
			print("{} {} {}".format(string,type(variable),[format(ele,'01x') for ele in variable]))
class Stack:
	def __init__(self):
		self.stack = ["main"]
		self.line_from = ["-"]

	def jmp(self,line_from,name,line_to):
		self.stack.append(name)
		self.line_from.append(line_from)
		print("## jump ## from {} to {} {}".format(line_from,name,line_to))
	def rtn(self):
		if len(self.stack) > 0:
			aa = self.stack.pop(-1)
			line_from = self.line_from.pop(-1)
			print("## back ## {} {} ".format(self.stack[-1],line_from))
		else:
			print("## stay ## {}".format(self.stack[0]))

if __name__ == '__main__':
	a = chr(0x40)+chr(0x89) + chr(0x40)+chr(0x89)
	a = six.b(a)
	a = numpy.frombuffer(a,dtype="uint32")
	a = a.tobytes()
	print("{} {}".format(a.__class__.__name__,a))
