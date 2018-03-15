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
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Cookie': '_guid=R235046d-c351-7518-8e2b-da9c5c7e8cd9; new_uv=1; PHPSESSID=6426bc4605987330f92854c4ea527559; __utma=253397513.1465259844.1521095861.1521095861.1521095861.1; __utmc=253397513; __utmz=253397513.1521095861.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); new_session=0; session_time=; init_refer=; als=0; isnew=1521095868361; __utmt=1; __utmb=253397513.7.10.1521095861',
	'Host': 'bbs.qyer.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
		}

def test():
	for i in range(1,5):
		url = 'http://bbs.qyer.com/forum-57-5-'+str(i)+'.html'
		print(url)
		response = requests.get(url,headers=headers,timeout=20,verify=False)
		html = response.content.decode('utf-8')
		selector = etree.HTML(html)
		links = selector.xpath('//dt[@class="title fontYaHei"]/a/@href')
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		s.keep_alive = False
		for link in links:
			# url = 'http://ask.qyer.com/question/3387775.html'
			header = {
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'zh-CN,zh;q=0.9',
				'Cache-Control': 'max-age=0',
				'Connection': 'keep-alive',
				'Cookie': '_guid=R235046d-c351-7518-8e2b-da9c5c7e8cd9; new_uv=1; __utma=253397513.1465259844.1521095861.1521095861.1521095861.1; __utmc=253397513; __utmz=253397513.1521095861.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); new_session=0; session_time=; init_refer=; als=0; isnew=1521095868361; PHPSESSID=30745789d7190404da54efedede076f6; __utmt=1; __utmb=253397513.11.10.1521095861',
				'Host': 'ask.qyer.com',
				'Upgrade-Insecure-Requests': '1',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
				}
			url = 'http:'+link
			if url not in url_list:
				url_list.append(url)
				r = requests.get(url,headers=header,timeout=5)
				print(r.status_code)		        
				html = r.content.decode("utf-8")  # 解码
				selector = etree.HTML(html)
				title = selector.xpath('//h2[@class="ask_detail_content_title qyer_spam_text_filter"]/text()')
				answers = selector.xpath('//div[@class="mod_discuss_box_text qyer_spam_text_filter"]/text()')
				like = selector.xpath('//a[@class="jsaskansweruseful useful_left"]/span/text()')
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				if len(answers)==0:
					pass
				else:
					for answer in answers:
						rb['答案'] = answer
						rb['问题'] = title
						rb['QID'] = link[24:-5]
						rb['LIKE'] = like[random.choice(range(len(like)))]
						rb['BEST'] = 1
						rb['IN'] = 1
						tmp = json.dumps(rb).replace(' ','')
						data = tmp.decode('unicode-escape')
						with codecs.open('qyer.txt','a+','utf-8') as f:
							f.write(str(data)+'\r\n')
							f.close()

				print(data)
			else:
				pass

test()