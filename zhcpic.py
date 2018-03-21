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
		links = selector.xpath('//div[@class="askmian"]/div[starts-with(@class,"head")]/a/@href')
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		s.keep_alive = False
		for link in links:
			# url = 'https://www.zhcpic.com/wenda/515478/'
			url = 'https://www.zhcpic.com'+link
			urls_list = []
			for i in range(1,6):
				urls_list.append(url+str(i)+'.html')		
			for url in urls_list:
				r = requests.get(url,headers=headers,timeout=20)
				print(r.status_code)		        
				html = r.content.decode("utf-8")  # 解码
				selector = etree.HTML(html)
				urls = selector.xpath('//div[@class="title_2"]/a/@href')
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				if urls ==[]:
					pass
				else:
					
					for url_url in urls:
						if url_url not in url_list:
							url_list.append(url_url)
							id_ = url_url[29:-5]
							url = 'http:'+url_url
							print(url)
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
							html = r.content.decode("utf-8")  # 解码
							selector = etree.HTML(html)
							title = selector.xpath('//div[@class="Tions"]/text()')[0]
							desc  = selector.xpath('//div[@class="ques-text u-clearfix"]/text()')
							if desc == []:
								desc = ''
							else:
								desc = desc[0]
							answers = selector.xpath('//div[@class="word"]')
							relations = selector.xpath('//ul[@class="wd-bot"]')[1].xpath('./li/a/text()')
							for relation in relations:
								with codecs.open('zhcpic_question_question.txt','a+','utf-8') as f1 :
									if desc == '':
										s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+'\t'+relation).strip().replace('\n','').replace('\r','')
										f1.write(s+'\r\n')
										f1.close()
									else:
										s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+relation).strip().replace('\n','').replace('\r','')
										f1.write(s+'\r\n')
										f1.close()
							requests.adapters.DEFAULT_RETRIES = 5
							s = requests.session()
							s.keep_alive = False
							# if len(answers)==0:
							# 	pass
							# else:
							# 	for answer in answers[:-1]:
							# 		if answer == '' :
							# 			pass
							# 		else:
							# 			answer = answer.xpath('string(.)').strip()
							# 			with codecs.open('zhcpic_question_answer.txt','a+','utf-8') as f:
							# 				if desc == '':
							# 					s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+'\t'+answer+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
							# 					f.write(s+'\r\n')
							# 					f.close()
							# 				else:
							# 					s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+answer+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
							# 					f.write(s+'\r\n')
							# 					f.close()



test()