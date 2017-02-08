#!/usr/bin/python3.4 
# -*- coding: utf-8 -*-
#
 
import urllib, os, random, shutil, copy

mp3=[]
#~ os.mkdir('5000')
five=100
#загружаем mp3, формируем |word - слово.mp3|
def Dow():
	o_file=open('1.txt', 'a+')
	print 1
	read_file=o_file.readlines()
	print 2
	
	for i in read_file:
		print 3
		destination = i.split(" - ")[0]+" - "+i.split(" - ")[1][:-1]+'.ogg'
		url = 'https://tts.voicetech.yandex.net/generate?text='+i.split(" - ")[0]+'&format=opus&lang=en-US&speaker=jane&key=f593fa88-b2a8-4c3e-8f12-834b060c722c&speed=0.1&emotion=good'
		urllib.urlretrieve(url, destination)
	print "загрузка +"


#создаем список файлов .ogg рандомный
def Ogg():
	for i in os.listdir("."):
		if "ogg" in i:
			mp3.append(i)
	#random.shuffle(mp3)

#добавляем тишину в mp3 файлы
#hush=open('hush', 'r'); a=hush.readlines()
#for i in mp3:
#	filmp3=open(i, 'a')
#	filmp3.writelines(a)
#	filmp3.close()
#print "тишина +"		

# создание директорий и заполняем файлами 1,2,3..200
def MkDir():
	"""
	Traceback (most recent call last):
	File "ya-5000.py", line 84, in <module>
	MkDir()
	File "ya-5000.py", line 49, in MkDir
	if len(os.listdir(str(z2))) < 10:
	OSError: [Errno 2] No such file or directory: '11'

	"""
	z=1
	z2=1
	while z < 10:
		os.mkdir(str(z))
		z+=1

	while z2 < five:
		if len(os.listdir(str(z2))) < 10:
			shutil.move(mp3.pop(0), str(z2))
		if len(os.listdir(str(z2))) == 10:
			z2+=1
	
	audio_dir=range(five)
	for i in audio_dir:
		shutil.move(str(i), '5000')
	
	print "файлы в норках +"


# создание файлов вида ang - russ, ang, russ
def ListFile():
	for i in os.listdir("./5000"):
		for ii in os.listdir("./5000/"+i):
			print ii[:-4]
			ang_rus_file=open('./5000/'+i+'/ang-rus.txt', 'a')
			ang_rus_file.write(ii[:-4]+'\n')
			ang_rus_file.close()
			
			a = ii.split(' - ')
			
			ang_rus_file=open('./5000/'+i+'/ang.txt', 'a')
			ang_rus_file.write(a[0]+'\n')
			ang_rus_file.close()
			
			ang_rus_file=open('./5000/'+i+'/rus.txt', 'a')
			ang_rus_file.write(a[-1][:-4]+'\n')
			ang_rus_file.close()
			print a[0]
			print a[-1][:-4]

#~ Dow()
#~ Ogg()
#~ MkDir()
ListFile()
