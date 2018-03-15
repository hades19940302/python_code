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
pro = ['112.95.56.203:8118',
		'222.76.187.42:8118',
		'221.224.49.237:3128',
		'113.105.201.31:3128',
		'1.196.55.187:61202',
		'27.215.245.246:61234',
		'61.135.217.7:80',
		'122.114.31.177:808',
		'180.113.45.132:8118',
		'183.143.53.87:61234',
		'116.55.77.81:61202',
		'27.19.77.33:61202',
		'183.23.75.66:61234',
		'59.48.148.226:61202',
		'221.224.49.237:3128']

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

def test():
	for i in range(1):
		url = 'https://www.zhcpic.com/riben/'
		response = requests.get(url,headers=headers,timeout=20,verify=False)
		html = response.content.decode('utf-8')
		selector = etree.HTML(html)
		links = selector.xpath('//div[@class="askmian"]/ul/li/a/@href')
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		s.keep_alive = False
		for link in links:
			# url = 'https://www.zhcpic.com/wenda/515478/'
			url = 'http:'+link
			r = requests.get(url,headers=headers,timeout=20)		        
			html = r.content.decode("utf-8")  # 解码
			selector = etree.HTML(html)
			urls = selector.xpath('//div[@class="title_2"]/a/@href')
			requests.adapters.DEFAULT_RETRIES = 5
			s = requests.session()
			s.keep_alive = False
			for url_url in urls:
				if url_url not in url_list:
					url_list.append(url_url)
					url = 'http:'+url_url
					header = {
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
						'Accept-Encoding': 'gzip, deflate, br',
						'Accept-Language': 'zh-CN,zh;q=0.9',
						'Cache-Control': 'max-age=0',
						'Connection': 'keep-alive',
						'Cookie': 'tp_sid=7fed5ab240a624d7; Hm_lvt_d7f4104c23e10d73303b198308c9b82d=1521098959; Hm_lpvt_d7f4104c23e10d73303b198308c9b82d=1521100326',
						'Host': 'www.zhcpic.com',
						'Upgrade-Insecure-Requests':' 1',
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
						}
					r = requests.get(url,headers=headers,timeout=20)
					print(r.status_code)
					print(url)		        
					html = r.content.decode("utf-8")  # 解码
					selector = etree.HTML(html)
					title = selector.xpath('//div[@class="Tions"]/text()')
					answers = selector.xpath('//div[@class="word"]/text()')
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					if len(answers)==0:
						pass
					else:
						for answer in answers:
							rb['答案'] = answer
							rb['问题'] = title
							print(type(answer))
							rb['QID'] = url_url[29:-5]
							rb['LIKE'] = 0
							rb['BEST'] = 1
							rb['IN'] = 1
							tmp = json.dumps(rb).replace(' ','')
							data = tmp.decode('unicode-escape')
							with codecs.open('zhcpic.txt','a+','utf-8') as f:
								f.write(str(data)+'\r\n')
								f.close()

			else:
				pass

test()