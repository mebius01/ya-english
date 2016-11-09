#!/usr/bin/python3.4 
# -*- coding: utf-8 -*-
#
 
import urllib, os, random, shutil, copy

z=1
z2=1
mp3=[]

##загружаем mp3, формируем |word - слово.mp3|
#o_file=open('1.txt', 'a+')
#read_file=o_file.readlines()

#for i in read_file:
	#destination = i.split(" - ")[0]+" - "+i.split(" - ")[1][:-1]+'.mp3'
	#url = 'https://tts.voicetech.yandex.net/generate?text='+i.split(" - ")[0]+'&format=mp3&lang=en-US&speaker=jane&key=2f6ede27-aaaf-42a1-a95b-34c67fc3fc9b&speed=0.1&emotion=good'
	#urllib.urlretrieve(url, destination)

#print "загрузка +"

#создаем список файлов .MP3 рандомный
for i in os.listdir("."):
	if "mp3" in i:
		mp3.append(i)
random.shuffle(mp3)

##добавляем тишину в mp3 файлы
#mp3b=copy.deepcopy(mp3)
#hush=open('hush', 'r'); a=hush.readlines()
#for i in mp3b:
	#filmp3=open(mp3b.pop(0), 'a')
	#for ii in a:
		#filmp3.writelines(ii)
	#filmp3.close()

#print "тишина +"		

while z < 250:
	os.mkdir(str(z))
	z+=1


#заполняем файлами директории 1,2,3..200
while z2 < 250:
	if len(os.listdir(str(z2))) < 20:
		shutil.copy(mp3.pop(0), str(z2))
	if len(os.listdir(str(z2))) == 20:
		z2+=1

print "файлы в норках"
