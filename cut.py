#!/usr/bin/env python
# coding=utf-8
# author=hades
# oshiete urls

import threadpool as tp
import codecs
mingan_list = []
def test(xxx):
	with codecs.open('ctrip_question_question.txt','rb') as f :
		for line in f.readlines():
			f3 = open('min.txt','rb')
			for m in f3.readlines(): 
				if line.find(m.strip()) == (-1):
					hang = line
				else:
					pass

			f2 = open('ctrip_question_question_min.txt','a+')
			f2.write(hang.replace('\r',''))
			f2.close()

		f.close()
		f3.close()

def test2():
	with codecs.open('zhcpic_question_answer_min.txt','rb') as f :
		f2 = open('zhcpic_question_answer_min_2.txt','a+')
		for line in f.readlines():
			if line.find('更多关于日本旅游的单词请进入翻译频道查看') == (-1):
				f2.write(line.replace('\r',''))

		f.close()
		f2.close()

args = ['xxxx','aaa','a']
pool = tp.ThreadPool(20)
reqs = tp.makeRequests(test, args)
[pool.putRequest(req) for req in reqs]
pool.wait()
		
