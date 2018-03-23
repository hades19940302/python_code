#!/usr/bin/env python
# coding=utf-8
# author=hades
# oshiete urls
from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
import lxml
import requests
from lxml import etree
import json
import codecs
import sys
import random
import threadpool as tp
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
rb = {}

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'tp_sid=7fed5ab240a624d7; Hm_lvt_d7f4104c23e10d73303b198308c9b82d=1521098959; Hm_lpvt_d7f4104c23e10d73303b198308c9b82d=1521099405',
	'Host': 'www.zhcpic.com',
	'Referer': 'https://www.zhcpic.com/admin/',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
		}

urls = ['https://www.zhcpic.com/riben/jiudian/','https://www.zhcpic.com/riben/jipiao/','https://www.zhcpic.com/riben/jingdian/','https://www.zhcpic.com/riben/baoxian/',
		'https://www.zhcpic.com/riben/gouwu/','https://www.zhcpic.com/riben/meishi/','https://www.zhcpic.com/riben/xianlu/','https://www.zhcpic.com/riben/menpiao/','https://www.zhcpic.com/riben/tianqi/','https://www.zhcpic.com/riben/qianzheng/'

	
	]
def test(url):
	for i in range(6):
		url_r = url + str(i)+'.html'
		print(url_r)
		response = requests.get(url_r,headers=headers,timeout=20,verify=False)
		html = response.content.decode('utf-8')
		selector = etree.HTML(html)
		links = selector.xpath('//div[@class="title_2"]/a/@href')
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		s.keep_alive = False
		for link in links :

			with codecs.open('zhcpic_url_list.txt','a+','utf-8') as f:
				f.write('https:'+link+'\r\n')
				f.close()
pool = tp.ThreadPool(2)
reqs = tp.makeRequests(test, urls)
[pool.putRequest(req) for req in reqs]
pool.wait()

