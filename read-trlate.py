#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Прости меня Кнут
Прости меня Вирт
Ибо я грешен 
Грех мой велик
"""

import os, re
from itertools import groupby

tex=open('text.txt', 'r')
tex_split=tex.readline()
tex_split=tex_split.split(" ")
new_x = list(set(tex_split))
tex.close()


def WhileWord():
	x=[]
	y=[]
	zero=1
	while zero < 500:
		a=os.listdir("./5000/"+str(zero))
		for i in a:
			result = re.search('^\w*\S', i)
			x.append(result.group(0))
			y.append(os.path.abspath(i))
		zero=zero+1
	return x, y

print type(WhileWord())

tex_list=[]
for i in new_x:
	for ii in WhileWord()[0]:
		if i == ii:
			tex_list.append((i, ii, WhileWord()[0].index(ii), WhileWord()[1][WhileWord()[0].index(ii)]))
			#~ print i, ii, WhileWord()[0].index(ii), WhileWord()[1][WhileWord()[0].index(ii)]

for i in list(set(tex_list)):
	for ii in i:
		print ii






#~ q=len(tex_split)-1
#~ while q >= 0:
	#~ WhileWord(tex_split[q])
	#~ q=q-1
	



