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
c=0 # Убрать

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
print(len(tex_split))

# поиск соответсвий, если  'just' == 'just' то just - просто.ogg из db_dir копируем в working_dir
el_in_db=[]
for i in os.listdir(db_dir):
	for ii in tex_split:
		result = re.search('(\S+)', i)
		if ii == result.group(0):
			el_in_db.append(ii)
			c=c+1 # Убрать
			#~ shutil.copy2(db_dir+i, working_dir) !!!раскоментить
			print db_dir+i, ii # !!!!вывод полного пути к найденому файлу Заменить на копирование в working_dir
print(c) # Убрать

# удаляем дубликаты 
el_in_db_new=list(set(el_in_db))

# удалить из грязного списка tex_split найденные элементы, tex_split становится рабочим списком для поиска перевода
for i in el_in_db_new:
	tex_split.remove(i)

print(tex_split) # Убрать
# получить перевод с translate.yandex.net. Загружаем ogg с tts.voicetech.yandex.net. Формируем word - слово.ogg
#~ for i in tex_split:
	#~ r = requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20171127T133350Z.e60c3c9b07c632de.6feca9afc681cd8810631df190fe1bbd40eb3cd4",
	#~ data={'text':i, 'lang':"en-ru"})
	#~ destination = i+' - '+(r.json().get('text')[0])+'.ogg'
	#~ url = 'https://tts.voicetech.yandex.net/generate?text='+i+'&format=opus&lang=en-US&speaker=jane&key=f593fa88-b2a8-4c3e-8f12-834b060c722c&speed=1&emotion=good'
	#~ urllib.urlretrieve(url, destination)
	#~ shutil.copy2(destination, working_dir)
	#~ shutil.move(destination, db_dir)
	#~ print destination
	#~ print "загрузка +"


