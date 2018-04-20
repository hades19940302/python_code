#!/usr/bin/env python
# coding=utf-8
# author=hades
# oshiete urls
from __future__ import print_function
from __future__ import division
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
import gzip
import StringIO
import time
import threadpool as tp
import urllib2
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
url_list=[]
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
from requests.adapters import HTTPAdapter
from time  import sleep
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
	}
urls = []
def test():
	f1 = open('by_2018_04_19_ids.txt','rb')
	for line in f1.readlines():
		id_ = line.replace('\r','').replace('\n','')
		url = 'https://zhidao.baidu.com/question/'+id_+'.html'
		# while True:
		try:
			response = requests.get(url,headers=headers,verify=False,timeout=5)
			html = response.content
			html = re.sub(r'<br[ ]?/?>', '\n', html)
			selector = etree.HTML(html)
			urls_rq = selector.xpath('//a[@class="question-list zd-symbol-item"]/@href')
		except:
			print(url)

		for urls_rq in urls_rq:
			if urls_rq not in urls:
				urls.append(urls_rq)
				with codecs.open('by_2018_04_19_qr_urls.txt','a','utf-8') as f1:
					f1.write(urls_rq+'\n')
					f1.close()
test()