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
	'Cookie': 'tp_sid=7fed5ab240a624d7; Hm_lvt_d7f4104c23e10d73303b198308c9b82d=1521098959,1521598007,1521612944,1521775183; tp_lastrefresh=1; Hm_lpvt_d7f4104c23e10d73303b198308c9b82d=1521777085',
	'Host': 'm.zhcpic.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		}

def test():
	f1 = open('zhcpic_url_list.txt','rb')
	for url in f1.readlines():
		id_ = url[29:-5]
		if id_ not in id_list:
			id_list.append(id_)
			url = 'https://m'+url[11:]
			print(url)
			while True:
				try:
					r = requests.get(url,headers=headers,timeout=50,verify=False)
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					break


				except:
					print('let us go  sleep!!!')
					sleep(5)
					print('ogo')
					continue	
			html = r.content.decode("utf-8")  # 解码
			html = re.sub(r'<br[ ]?/?>', '\n', html)
			selector = etree.HTML(html)
			print(html)
			question_res = selector.xpath('//div[@class="news-item xg-question"]/ul/li/a')
			question = selector.xpath('//div[@class="char-item-con"]')[0].xpath('string(.)').strip()
			question_desc = selector.xpath('//div[@class="char-item-intro"]')[0].xpath('string(.)').strip()
			if question_desc == '':
				desc = ''
			else:
				desc =question_desc
			for question_re in question_res:
				with codecs.open('zhcpic_question_question.txt','a+','utf-8') as f1 :
					if desc == '':
						s = ('1'+'\t'+'qid:'+id_+'\t'+question+'\t'+question_re.xpath('string(.)').strip()).strip().replace('\n','').replace('\r','')
						f1.write(s+'\r\n')
						f1.close()
					else:
						s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+relation).strip().replace('\n','').replace('\r','')
						f1.write(s+'\r\n')
						f1.close()

			answers = selector.xpath('//div[@class="comment-item-con"]')
			for answer in answers:
					answer = answer.xpath('string(.)').strip()
					with codecs.open('zhcpic_question_answer.txt','a+','utf-8') as f:
						if desc == '':
							s = ('1'+'\t'+'qid:'+id_+'\t'+question+'\t'+answer+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
							f.write(s+'\r\n')
							f.close()
						else:
							s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+answer+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
							f.write(s+'\r\n')
							f.close()


test()				