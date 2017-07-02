#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re

tex=open('text.txt', 'r')
tex_split=tex.readline(); tex_split=tex_split.split(" ")
tex.close()

def WhileWord():
	x=[]
	zero=1
	while zero < 500:
		a=os.listdir("./5000/"+str(zero))
		for i in a:
			x.append(i)
		zero=zero+1
	return x


for i in tex_split:
	for ii in WhileWord():
		if i == ii:
			print i, ii





#~ q=len(tex_split)-1
#~ while q >= 0:
	#~ WhileWord(tex_split[q])
	#~ q=q-1
	



