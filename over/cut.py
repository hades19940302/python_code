#!/usr/bin/env python
# coding=utf-8
# author=hades
# oshiete urls

import threadpool as tp
import codecs
mingan_list = []
def test():
	file_name_list = ['ctrip_question_answer','ctrip_question_question','lvmama_question_answer','lvmama_question_question','oshiete_question_answer','oshiete_question_question','tuniu_question_answer',
						'zhcpic_question_answer','zhcpic_question_question'
		]
	f3 = open('min.txt','rb')
	min_list = []
	for m in f3.readlines():
		m = m.strip().replace(' ','').replace('\n','').replace('\r','')
		if m == '':
			pass
		else:

			min_list.append(m.strip())
			print(m)

	f3.close()
	f4 = open('offensive_words.txt','rb')
	off_list = []
	for m in f4.readlines():
		m = m.strip().replace(' ','').replace('\n','').replace('\r','')
		if m == '':
			pass
		else:

			off_list.append(m.strip())
			print(m)	
	for file_name in file_name_list:
		file_name_ = file_name+'.txt'
		with codecs.open(file_name_,'rb') as f :
			for line in f.readlines():
				for m in off_list: 
					if  m in line:
						pass
					else:
						hang = line
				file_name_2 = file_name_+'_min_2.txt'
						
				f2 = open(file_name_2,'a+')
				f2.write(hang.replace('\r',''))
		f2.close()

		f.close()

def test2():
	with codecs.open('zhcpic_question_answer_min.txt','rb') as f :
		f2 = open('zhcpic_question_answer_min_2.txt','a+')
		for line in f.readlines():
			if line.find('更多关于日本旅游的单词请进入翻译频道查看') == (-1):
				f2.write(line.replace('\r',''))

		f.close()
		f2.close()

test()
# args = ['xxxx','aaa','a']
# pool = tp.ThreadPool(20)
# reqs = tp.makeRequests(test, args)
# [pool.putRequest(req) for req in reqs]
# pool.wait()
		
