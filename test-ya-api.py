#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, shutil, urllib, requests, copy

soft_dir=os.path.abspath('.')+'/' #директория программы
db_dir=soft_dir+'Db_dir/' # словарь на 5000 db_dir
working_dir=soft_dir+'Working_dir/' # что нашли кладем в working_dir

# создание директорий и заполняем файлами 1,2,3..200
def MkDir():
	ogg_file=os.listdir(working_dir)
	work_len=len(os.listdir(working_dir))
	work_dir=work_len/12
	if work_len % 12 > 0:
		work_dir+=1
	work_dir2=copy.deepcopy(work_dir)
	#~ z=1
	#~ while z <= work_dir:
		#~ os.mkdir(str(work_dir))
		#~ work_dir-=1

	while work_dir2 >= 1:
		if len(str(work_dir2)) < 12:
			shutil.move(working_dir+ogg_file.pop(0), str(work_dir2))
			#~ work_dir2-=1
	#~ while z2 < work_dir:
		#~ if len(os.listdir(str(z2))) < 12:
			#~ shutil.move(mp3.pop(0), str(z2))
		#~ if len(os.listdir(str(z2))) == 12:
			#~ z2+=1
	
	#~ audio_dir=range(five)
	#~ for i in audio_dir:
		#~ shutil.move(str(i), '5000')
	#~ print work_ogg
	print(ogg_file)
	print(work_dir)
	print(work_dir)
	print "файлы в норках +"
MkDir()
	
