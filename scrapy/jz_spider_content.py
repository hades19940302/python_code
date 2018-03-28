#!/usr/bin/env python
# coding=utf-8
# author=hades
# 实现爬虫驾照考试题
from bs4 import BeautifulSoup
import urllib 
import requests
import pymysql
from multiprocessing.dummy import Pool as ThreadPool

def test():
	r = requests.get('http://www.ccyp.com/home/drivingtest?gclid=CjwKEAjwhrzLBRC35--F9sSH0FASJAD5obJ1FgzkZlm-0fKJACOXWBnF_OjYEXm5Pw1s7h_ZEbwW_BoC80vw_wcB###')
	# r = urllib.open('http://www.ccyp.com/home/drivingtest?gclid=CjwKEAjwhrzLBRC35--F9sSH0FASJAD5obJ1FgzkZlm-0fKJACOXWBnF_OjYEXm5Pw1s7h_ZEbwW_BoC80vw_wcB')
	# print r.content
	html_doc = ''
	with open('1.html', 'r') as f:
		soup = BeautifulSoup(f,'html.parser',from_encoding='utf-8')
		# print soup.find_all('a')
		# links = soup.find_all('a')
		all_divs = soup.find_all('div',class_='q-title')
		all_divs_ = soup.find_all('div'.class_='row-fluid q-wrap')
		all_input = soup.find_all('input',class_='q-select')
		for i,div in enumerate(all_divs):
			content = div.get_text()
			if i <10:
				t_id = content[:1].strip()
				content = content[5:-1].strip()
			elif i<100:
				t_id = content[:2].strip()
				content = content[6:-1].strip()
			else:
				t_id = content[:3].strip()
				content = content[7:-1].strip()
			print content,t_id
			try:
				conn = pymysql.connect(host='localhost', user='root', passwd='hades', charset='utf8mb4')
				cur = conn.cursor()
			        # cur.execute('create database if not exists python')
				conn.select_db('csinla')
				cur.execute('UPDATE csinla_accounts_driveexamnation SET content=%s WHERE t_id=%s',[content,int(t_id)])
				"""
					没有这句都是zz
				"""
				print('更新成功！！')
				conn.commit()
				cur.close()
				conn.close()
			except Exception,e:
				print('链接数据库失败')
	# print all_divs
	# for link in links:
		# print link.name,link['href'],link.get_text()
	# answer_ids = []
	# index = 1
	# for input_ in all_input:
	# 	parent = input_.parent 
	# 	content = parent.get_text().strip()
	# 	# print input_
	# 	answer_id = input_['data-answerid']
	# 	# print div_.get_text()
	# 	if content == '' or  content == None:
	# 		pass
	# 	else:
	# 		content_ = content
	# 	t_id = input_['name'].strip()
	# 	t_id = int(t_id)
	# 	answer_ids.append(t_id)
	# 	if answer_ids.count(t_id) == 2:

	# 		try:
	# 			conn = pymysql.connect(host='localhost', user='root', passwd='hades', charset='utf8mb4')
	# 			cur = conn.cursor()
	# 	        # cur.execute('create database if not exists python')
	# 			conn.select_db('csinla')
	# 			cur.execute('UPDATE csinla_accounts_driveexamnation SET answer_b=%s WHERE t_id=%s',[content_,int(t_id)])
	# 			"""
	# 			没有这句都是zz
	# 			"""
	# 			print('更新成功！！')
	# 			conn.commit()
	# 			cur.close()
	# 			conn.close()
	# 		except Exception,e:
	# 			print('链接数据库失败')

	# 	else:
	# 		pass
		# print content_
		# print answer_id
	# for input_ in all_input:
	# 	answer_id = input_['data-answerid']
	# 	print answer_id
	# 	# content =  div.get_text()
		# print content
		# t_id = content[0:3]
		# content = content[7:-1]
		# print t_id.strip()
		# print content.strip()
		# try:
		# 	conn = pymysql.connect(host='localhost', user='root', passwd='hades', charset='utf8mb4')
		# 	cur = conn.cursor()
	 #        # cur.execute('create database if not exists python')
		# 	conn.select_db('csinla')
		# 	cur.execute('INSERT INTO csinla_accounts_driveexamnation(t_id,content)  VALUES (%s,%s)',[int(t_id),content])
		# 	"""
		# 	没有这句都是zz
		# 	"""
		# 	conn.commit()
		# 	cur.close()
		# 	conn.close()
		# except Exception,e:
		# 	print(e)
test()