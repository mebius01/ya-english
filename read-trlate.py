#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Прости меня Кнут
Прости меня Вирт
Ибо я грешен 
Грех мой велик
"""

import os, re, shutil
tex=open('text.txt').read().split('\n')
tex=str(tex)
tex_split = re.findall('([A-Za-z]+)', tex); tex_split=list(set(tex_split))

soft_dir=os.path.abspath('.')+'/'
db_dir=soft_dir+'Db_dir/'
working_dir=soft_dir+'Working_dir/'
print(soft_dir, db_dir, working_dir)

dic_tex_split={}
for i in tex_split:
	dic_tex_split[tex_split.index(i)] = i

#~ g_list=[]
#~ for i in os.listdir(db_dir):
	#~ result = re.search('(\S+)', i)
	#~ g_list.append([result.group(0), i])
	#~ 
#~ # g_list[0][1] = attraction - привлекательность | g_list[0][1] = attraction


el_in_db=[]
print len(tex_split)
for i in os.listdir(db_dir):
	for ii in tex_split:
		result = re.search('(\S+)', i)
		if result.group(0) == ii.lower():
			el_in_db.append(tex_split.index(ii))
			#~ print(db_dir+i)
print el_in_db

while len(el_in_db) > 0:
	del dic_tex_split[el_in_db.pop()]
	
print dic_tex_split
			#~ shutil.copy(db_dir+i, working_dir)


#~ def WhileWord():
	#~ x=[]
	#~ y=[]
	#~ zero=1
	#~ while zero < 500:
		#~ a=os.listdir("./5000/"+str(zero))
		#~ for i in a:
			#~ result = re.search('^\w*\S', i)
			#~ x.append(result.group(0))
			#~ y.append(os.path.abspath(i))
		#~ zero=zero+1
	#~ return x, y
#~ 
#~ print(WhileWord())

#~ for i in WhileWord()[1]:
	#~ shutil.copy2(i, r'/home/ivan/project/ya-english/5000-stipMP3')

#~ tex_list=[]
#~ for i in tex_split:
	#~ for ii in WhileWord()[0]:
		#~ if i == ii:
			#~ tex_list.append(WhileWord()[1][WhileWord()[0].index(ii)])
			#~ print i, ii, WhileWord()[0].index(ii), WhileWord()[1][WhileWord()[0].index(ii)]
#~ 
#~ 
#~ tex_list = list(set(tex_list))
#~ print(tex_list), len(tex_list)








#~ q=len(tex_split)-1
#~ while q >= 0:
	#~ WhileWord(tex_split[q])
	#~ q=q-1
	



