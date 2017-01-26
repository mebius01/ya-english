#!/usr/bin/python3.4 
# -*- coding: utf-8 -*-
#
 
import urllib, os, random, shutil, copy

z=1
z2=1
mp3=[]

#загружаем mp3, формируем |word - слово.mp3|
o_file=open('1.txt', 'a+')
read_file=o_file.readlines()

for i in read_file:
	destination = i.split(" - ")[0]+" - "+i.split(" - ")[1][:-1]+'.ogg'
	url = 'https://tts.voicetech.yandex.net/generate?text='+i.split(" - ")[0]+'&format=opus&lang=en-US&speaker=jane&key=f593fa88-b2a8-4c3e-8f12-834b060c722c&speed=0.1&emotion=good'
	urllib.urlretrieve(url, destination)
	

print "загрузка +"

#создаем список файлов .ogg рандомный
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

while z < 500:
	os.mkdir(str(z))
	z+=1


#заполняем файлами директории 1,2,3..200
while z2 < 500:
	if len(os.listdir(str(z2))) < 10:
		shutil.move(mp3.pop(0), str(z2))
	if len(os.listdir(str(z2))) == 10:
		z2+=1

print "файлы в норках +"
