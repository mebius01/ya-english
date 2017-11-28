#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Прости меня Кнут
Прости меня Вирт
Ибо я грешен 
И грех мой велик
"""


# получает файл с текстом. разделить строки по \n. преобразит верхний регистр в нижний
import os, re, shutil, urllib, requests
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

soft_dir=os.path.abspath('.')+'/' #директория программы
db_dir=soft_dir+'Db_dir/' # словарь на 5000 db_dir
working_dir=soft_dir+'Working_dir/' # что нашли кладем в working_dir
# print(soft_dir, db_dir, working_dir)

# поиск соответсвий, если  'just' == 'just' то just - верный, точный.ogg из db_dir копируем в working_dir

el_in_db=[]
for i in os.listdir(db_dir):
	for ii in tex_split:
		result = re.search('(\S+)', i)
		if ii == result.group(0):
			el_in_db.append(ii)
			print db_dir+i, ii # !!!!вывод полного пути к найденому файлу Заменить на копирование в working_dir
 
# удаляем дубликаты 
el_in_db_new=list(set(el_in_db))

# удалить из грязного списка tex_split найденные элементы, tex_split становится рабочим списком для поиска перевода и аудио
for i in el_in_db_new:
	tex_split.remove(i)


for i in tex_split:
	r = requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20171127T133350Z.e60c3c9b07c632de.6feca9afc681cd8810631df190fe1bbd40eb3cd4",
	data={'text':i, 'lang':"en-ru"})
	destination = i+' - '+(r.json().get('text')[0])+'.ogg'
	url = 'https://tts.voicetech.yandex.net/generate?text='+i+'&format=opus&lang=en-US&speaker=jane&key=f593fa88-b2a8-4c3e-8f12-834b060c722c&speed=1&emotion=good'
	urllib.urlretrieve(url, destination)
	print destination
	print "загрузка +"








































#~ https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20171127T133350Z.e60c3c9b07c632de.6feca9afc681cd8810631df190fe1bbd40eb3cd4&text=Learning how to take great photos is about more than just understanding how your camera works&lang=en-ru&format=plain&callback=callback

#~ text=Learning how to take great photos is about more than just understanding how your camera works

#~ otput
#~ callback({"code":200,"lang":"en-ru","text":["Как научиться делать отличные фотографии-это больше, чем просто понимание того, как ваша камера работает"]})

#~ https://translate.yandex.net/api/v1.5/tr.json/translate
 #~ ? [key=<API-ключ>]
 #~ & [text=<переводимый текст>]
 #~ & [lang=<направление перевода>]
 #~ & [format=<формат текста>]
 #~ & [options=<опции перевода>]
 #~ & [callback=<имя callback-функции>]


#~ http://translate.google.ru/translate_a/t?client=x&text=Learning&hl=en&sl=en&tl=ru

#~ https://github.com/z0rr0/ytapi  консольный переводчик с яндекс АПИ

#~ https://tech.yandex.ru/translate/doc/dg/concepts/About-docpage/ доки на ЯнАПИ переводчик

#~ https://pythoness.pp.ua/catalog/article/perevodchik-na-baze-python-i-storonnego-api/ Переводчик на базе Python и стороннего API

#~ for i in tex_split:
	#~ destination = i+'.ogg'
	#~ url = 'https://tts.voicetech.yandex.net/generate?text='+i+'&format=opus&lang=en-US&speaker=jane&key=f593fa88-b2a8-4c3e-8f12-834b060c722c&speed=1&emotion=good'
	#~ urllib.urlretrieve(url, destination)
	#~ print "загрузка +"

#~ https://tts.voicetech.yandex.net/generate?text=(((abstain)))&format=opus&lang=en-US&speaker=jane&key=f593fa88-b2a8-4c3e-8f12-834b060c722c&speed=1&emotion=good

#~ https://pypi.python.org/pypi/py-translate

"""Ключь API lingvolive YWQ4ZDhkZWItZmRmZC00NDEzLTkyMDgtMmQ5ZDhiM2UzODFmOjhjYzJmMDAyY2RlMzRmZmI4MzAwOWI5ODZlMzk4NjU4 """


# Формируеn словарь {0: 'yard', 1: 'all', 2: 'just', 3: 'dreamed', 4: 'over', 5: 'move'} 
#~ dic_tex_split={}
#~ for i in tex_split:
	#~ dic_tex_split[tex_split.index(i)] = i
#~ print dic_tex_split


# Формируеn словарь из db_dir {'abhor': 'abhor - питать отвращение.ogg', 'representative': 'representative - представитель.ogg'}
#~ g_list={}
#~ for i in os.listdir(db_dir):
	#~ result = re.search('(\S+)', i)
	#~ g_list[result.group(0)] = i
#~ print g_list


# Формируеn список g_list[0][1] = attraction - привлекательность | g_list[0][0] = attraction
#~ g_list=[]
#~ for i in os.listdir(db_dir):
	#~ result = re.search('(\S+)', i)
	#~ g_list.append([result.group(0), i])
#~ print g_list[0][0]

#~ 
#~ while len(el_in_db) > 0:
	#~ del dic_tex_split[el_in_db.pop()]
	#~ 
#~ print dic_tex_split
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
	



