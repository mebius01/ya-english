#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Прости меня Кнут
Прости меня Вирт
Ибо я грешен 
И грех мой велик
"""
import os, re, shutil, urllib, requests, copy

soft_dir=os.path.abspath('.')+'/' #директория программы
db_dir=soft_dir+'Db_dir/' # словарь на 5000 db_dir
working_dir=soft_dir+'Working_dir/' # что нашли кладем в working_dir

# получает файл с текстом. разделить строки по \n. преобразит верхний регистр в нижний
tex=open('text.txt').read().split('\n')
tex=str(tex).lower()

# удалить ,"':;. удалить строки > 3 симв. преобразить строку в список ['yard', 'all', 'just', 'dreamed', 'over', 'move']
tex_split = re.findall('([A-Za-z]+)', tex); tex_split=list(set(tex_split))
i=0
while i < len(tex_split):
	if len(tex_split[i]) < 3:

		del tex_split[i]
	else:
		i += 1

# поиск соответсвий, если  'just' == 'just' то just - просто.ogg из db_dir копируем в working_dir
el_in_db=[]
for i in os.listdir(db_dir):
	for ii in tex_split:
		result = re.search('(\S+)', i)
		if ii == result.group(0):
			el_in_db.append(ii)
			shutil.copy2(db_dir+i, working_dir) # !!!раскоментить
			print db_dir+i, ii # !!!!вывод полного пути к найденому файлу Заменить на копирование в working_dir

# удаляем дубликаты 
el_in_db_new=list(set(el_in_db))

# удалить из грязного списка tex_split найденные элементы, tex_split становится рабочим списком для поиска перевода
for i in el_in_db_new:
	tex_split.remove(i)

def Download():
	"""
	получить перевод с translate.yandex.net. Загружаем ogg с tts.voicetech.yandex.net. Формируем word - слово.ogg
	"""
	for i in tex_split:
		r = requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20171127T133350Z.e60c3c9b07c632de.6feca9afc681cd8810631df190fe1bbd40eb3cd4",
		data={'text':i, 'lang':"en-ru"})
		destination = i+' - '+(r.json().get('text')[0])+'.ogg'
		url = 'https://tts.voicetech.yandex.net/generate?text='+i+'&format=opus&lang=en-US&speaker=jane&key=f593fa88-b2a8-4c3e-8f12-834b060c722c&speed=1&emotion=good'
		urllib.urlretrieve(url, destination)
		shutil.copy2(destination, working_dir)
		shutil.move(destination, db_dir)
		print destination
		print "загрузка +"


def MkDir():
	"""
	cздание директорий 1 2 3 4 5 итд, заполняем файлами ogg
	"""
# создание списка с прямым путем к ogg
	ogg_file=[]
	for i in os.listdir(working_dir):
		ogg_file.append(working_dir+i)

	work_len=len(ogg_file); work_dir=work_len/12
	if work_len % 12 > 0:
		work_dir+=1
	work_dir2=copy.deepcopy(work_dir)

# создание директорий 1,2,3..200
	z=1
	while z <= work_dir:
		os.mkdir(str(work_dir))
		work_dir-=1

# и заполняем файлами	
	z=1
	try:
		while z < work_dir2+1:
			if len(os.listdir(str(z))) < 12:
				shutil.copy2(ogg_file.pop(0), str(z))
			if len(os.listdir(str(z))) == 12:
				z+=1
	except IndexError:
		print ""

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

MkDir()
#~ Download()
