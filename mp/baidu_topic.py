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

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))


headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',	
	'Connection': 'keep-alive',
	'Cookie': 'BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1446_21101_22158; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1521090106; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1521090106; PSINO=2; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1521090535; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1521090535',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
	}

topics_list = ['日本旅游']
topics_list_has_read= []
def test(xxx):
	while True:
		for title in topics_list:
			if title not in topics_list_has_read:

				url = 'https://m.baidu.com/recsys/ui/api/rs?query='+title+'&title='+title+'&url=https%3A%2F%2Fzhidao.baidu.com%2Fsearch%3Fword%3D%25C8%25D5%25B1%25BE%25BE%25C6%25B5%25EA%26ie%3Dgbk%26site%3D-1%26sites%3D0%26date%3D0%26pn%3D750&ak=ZQ4m31EXvKem1HPYzaK8Ekq6opqfhKFK&pc=1&charset=gbk&contentTitleText=%C8%A5%CD%F8%D2%B3%CB%D1%CB%F7&entityNum=9&tn=SE_PcZhidaoqwyss_e1nmnxgw&random=1826560278897984'
				response = requests.get(url,headers=headers,timeout=20,verify=False)
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				html = response.content # 解码
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				selector = etree.HTML(html)
				topics = selector.xpath('//span[@class="c-span4 c-line-clamp1 rw-item"]/a')
				for topic in topics:
					topic = topic.xpath('string(.)').strip()
					topics_list_has_read.append(topic)
					# url = 'https://zhidao.baidu.com/question/1732180052597957147.html'
					with codecs.open('baiduzhidao_topics_list_1.txt','a+','utf-8') as f :
							f.write(topic+'\r\n')
							f.close()

args = ['xxxx']
pool = tp.ThreadPool(20)
reqs = tp.makeRequests(test, args)
[pool.putRequest(req) for req in reqs]
pool.wait()
		