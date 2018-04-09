#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/3/30 15:22
import sys
import re
reload(sys)  
sys.setdefaultencoding('utf8') 
import codecs
import threadpool as tp
ids = []
# def test():
# 	f = codecs.open('jiang2qq.txt','rb','utf-8')
# 	for line in f.readlines():
# 		try:
# 			tt = line.index('\t',2)
# 			index = line[6:tt]
# 			if index not in ids:
# 				ids.append(index)
# 				tt2 = line.index('\t',(tt+1))
# 				print(line[:(tt2)])
# 				f1= codecs.open('zhidao_question_to_answer_man.txt','rb','utf-8')
# 				for line1 in f1.readlines():
# 					if index in line1:
# 						f3 = codecs.open('zhidao_question_to_answer_man_new_3.txt','a','utf-8')
# 						s= line1.replace('\r','').replace(line1[:tt2],line[:tt2])
# 						f3.write(s)
# 						f3.close()
# 					else:
# 						continue

# 				f1.close()
# 			else:
# 				continue
# 		except:
# 			continue
# 	f.close()


mingan_list = []
def test():
	with codecs.open('part1.txt','rb') as f :
		for line in f.readlines():
			f3 = open('min2.txt','rb')
			line = line.replace('\n','').replace('\r','').strip()
			for m in f3.readlines(): 
				m = m.replace('\n','').replace('\r','').strip()
				if m in line:
					pass
				else:
					hang = line

			f2 = open('part1_min.txt','a')
			f2.write(hang+'\n')
			f2.close()

		f.close()
		f3.close()


def getCoding(strInput):

	if isinstance(strInput, unicode):
		return "unicode"
	try:
		strInput.decode("utf8")
		return 'utf8'
	except:
		pass
	try:
		strInput.decode("gbk")
		return 'gbk'
	except:
		pass


ids_qid = []

def filter_by_qid():
	f = open('li7144.txt','rb')
	for line in f.readlines():
		tt = line.index('\t',2)
		id_ = line[6:tt]
		flag = line[:-line[::-1].index('\t')]
		if id_ not in ids_qid:
			answers = []
			ids_qid.append(id_)
			f1 = open('part1_min.txt','rb')
			for line1 in f1.readlines():
				if line1.find(id_) != -1:
					if line1[len(flag):].replace('\r', '') not in answers:
						answers.append(line1[len(flag):].replace('\r', ''))
						f = open('part1_min_filter_by_qid_3.txt','a')
						f.write(flag+line1[len(flag):].replace('\r',''))
						f.close()

			f1.close()



	f.close()

filter_by_qid()







filter_by_qid()






mingan = [u'买B啊:18岁的日本妞30元RMB一炮',u'充气娃娃',u'日本人的床上好玩，日本人的鸡巴大去了把你尻死不用回来了',u'真它妈是个汉奸',u'红灯一条街呗',u'汉奸',
		u'邓超和孙俪旅游到日本是不是卖国行为！',u'八嘎鸭路',u'我们要消灭日本',u'傻逼',u'干小姐',u'日本鬼子国',u'去日本旅游的都是猪!是贱人!',
		u'我们要消灭日本',
		  u'你老母',]
topics = [u'日本',u'京都',u'富士山',u'横滨',u'奈良',u'冲绳',u'北海道',u'名古屋',u'福冈',u'神户',u'涩谷',u'新宿',u'札幌',u'洞爷湖',u'函馆',u'镰仓',
		  u'濑户内海', u'鹿儿岛', u'富良野', u'千叶', u'静冈', u'JR', u'新干线', u'银座', u'表参道', u'药妆店',]
def test2():
	with codecs.open('part2.txt','rb') as f :
		for line in f.readlines():
			line = line.replace('\n','').replace('\r','').strip()
			print(line)
			for  topic in topics:
				if line.find(topic) != -1:
					f1 = open('part2_min_topic.txt','a')
					f1.write(line+'\n')
					f1.close()
					break
				else:
					continue
				# line1 = line1.decode('utf8')topic

	f.close()

def test3():
	with codecs.open('part2_min_topic.txt','rb') as f:
		for line in f.readlines():
			line = line.replace('\n','').replace('\r','').strip()
			# line = line.decode('utf8')
			for  mingan_item in mingan:
				if line.find(mingan_item) != -1:
					flag = 1
					break

				else:
					hang = line
					flag = 0
					continue
			if flag == 0:

				f1 = open('part2_min.txt','a')
				f1.write(hang+'\n')
				f1.close()
				print(line)
			elif flag == 1:
				continue



	f.close()

