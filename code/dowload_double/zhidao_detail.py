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
	# 'Cookie': 'IKUT=4099; BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; locale=zh; H_PS_PSSID=1446_21101_22158; PSINO=2; pgv_pvi=4774521856; pgv_si=s6383790080; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1522048693,1522118202,1522121671,1522129987; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1522135292; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1522043824,1522047460,1522048637,1522135295; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1522135295',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
	}

header = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'no-cache',
	'Cookie': 'IKUT=9083; BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; locale=zh; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1521679018,1521700344,1521717685,1521723445; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1521723445; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1521624927,1521680045,1521700358,1521723528; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1521723528',
	'Host': 'zhidao.baidu.com',
	'Pragma': 'no-cache',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
	
	}

proxy_header = {
	'Host': 'ent.kuaidaili.com',
	'Connection': 'keep-alive',
	'Cache-Control': 'max-age=0',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	

	}

proxys = []
r_proxy=  requests.get('http://ent.kuaidaili.com/api/getproxy/?orderid=938176699822329&num=1000&quality=2&sort=1&format=json')
json_data = json.loads(r_proxy.content)
data = json_data['data']
proxy_list = data['proxy_list']

for proxy in proxy_list:
	if proxy not in proxys:
		proxys.append(proxy)


urls = []
def test(xx):
	f1 = open('urls.txt','rb')
	for url in f1.readlines():
		url = url.replace('\r','').replace('\n','')
		while True:
			try:
				response = requests.get(url,headers=headers,verify=False,timeout=5)
				html = response.content
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				selector = etree.HTML(html)
				urls_rq = selector.xpath('//a[@class="question-list zd-symbol-item"]/@href')
				break
			except:
				print(url)
				continue

		for urls_rq in urls_rq:
			if urls_rq not in urls:
				urls.append(urls_rq)
				with codecs.open('qr_urls_2018_04_17_10_11.txt','a','utf-8') as f1:
					f1.write(urls_rq+'\n')
					f1.close()



# test()











args = ['xxxx']
pool = tp.ThreadPool(20)
reqs = tp.makeRequests(test, args)
[pool.putRequest(req) for req in reqs]
pool.wait()


