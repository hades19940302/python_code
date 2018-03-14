#!/usr/bin/env python
# coding=utf-8
# author=hades
# 携程网日本相关信息爬取
import requests
from lxml import etree
import json
import datetime
import time
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
url='http://m.baidu.com/his?callback=json&type=3&pic=1&net=1&hisdata=[{"kw":"日本旅游","time":1520988178}]&_=1520988906089'
topics = []
def getItem():
	r = requests.get(url)
	json_data = json.loads(r.content[11:-2])
	for data in json_data['his']:
		start = url.index('kw')
		end = url.index('time')
		dt_time = datetime.datetime.now()
		un_time = time.mktime(dt_time.timetuple())
		un_time = str(un_time)[:-2]
		new_url = url[:72]+data+url[85:94]+un_time+url[104:]
		print new_url
		print un_time
		print start,end
		


getItem()