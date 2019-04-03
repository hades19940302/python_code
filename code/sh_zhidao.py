#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/3/30 15:22
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
import re
import threadpool as tp
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
from requests.adapters import HTTPAdapter
from time import sleep
from urllib import quote
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
	}

header = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

topics = []
topics_list = ['东京','大阪','京都','富士山','横滨','奈良','冲绳','北海道','名古屋','福冈','神户','涩谷',
 				'新宿','札幌','洞爷湖','函馆','镰仓','濑户内海','鹿儿岛','富良野','千叶','静冈',
 				]

topics_list_2 = ['饮食','好吃的','餐厅','购物','买','交通','地铁','JR','新干线','好玩的','景点','体验','经验','休闲','度假','樱花','红叶','温泉','银座','表参道','机场','滑雪','酒店','药妆店']
def test():
	for t in topics_list:
		for t2 in topics_list_2:
			topic = t + t2
			topics.append(topic)

	for top in topics:
		for i in range(0,770,10):
			url = 'https://zhidao.baidu.com/search?word='+top+'&pn='+str(i)
			while True:
				try:
					r = requests.get(url,headers=header,timeout=20,verify=False)
					requests.adapters.DEFAULT_RETRIES = 5
					print(r.content)
					s = requests.session()
					s.keep_alive = False
					break


				except:
					print('let us go  sleep!!!')
					sleep(20)
					print('ogo'+r.content)
					continue
			requests.adapters.DEFAULT_RETRIES = 5
			s = requests.session()
			s.keep_alive = False
			html = r.content # 解码
			html = re.sub(r'<br[ ]?/?>', '\n', html)
			selector = etree.HTML(html)
			links = selector.xpath('//dl[@class="dl"]/dt[@class="dt mb-4 line"]/a/@href')
			for link in links:
				# url = 'https://zhidao.baidu.com/question/1732180052597957147.html'
				link = link[:link.index('?fr')]
				print(link)
				with codecs.open('baiduzhidao_url_list_xuqiu.txt','a+','utf-8') as f :
						f.write(link+'\n')
						f.close()

test()