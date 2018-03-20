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
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}  # 构造浏览器头信息


def test():
	for i in range(1):
		url = 'http://www.mafengwo.cn/qa/ajax_qa/more?type=3&mddid=10183&tid=&sort=9&key=&page=0&time=2018-03-14+20%3A44%3A54'
		response = requests.get(url,headers=header,timeout=20,verify=False)

		json_data = json.loads(response.content)
		html = json_data['data']
		html = html['html']
		selector = etree.HTML(html)
		links = selector.xpath('//div[@class="title"]/a/@href')
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		s.keep_alive = False
		for link in links:
			url = 'http://www.mafengwo.cn'+link
			id_ = link[14:22]
			# url = 'http://www.mafengwo.cn/wenda/detail-9196334.html'
			if url not in url_list:
				url_list.append(url)
				r = requests.get(url,headers=header,timeout=5)
		        
				html = r.content.decode("utf-8")  # 解码
				selector = etree.HTML(html)
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				title = selector.xpath('//div[@class="q-title"]/h1/text()')[0].strip()
				desc = selector.xpath('//div[@class="q-desc"]/text()')
				related_qts = selector.xpath('//div[@class="related-qt"]/ul/li/a/text()')
				if desc == []:
					desc = ''
				else:
					desc = desc[0]				

				for related_qt in related_qts :
					with codecs.open('mafengwo_question_question.txt','a+','utf-8') as f:
						f.write('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+related_qt+'\r\n')
						f.close()					

				answers = selector.xpath('//div[starts-with(@class,"answer-item")]')
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				print(len(answers))

				# for answer in answers:
				# 	title_answer = answer.xpath('string(.)').strip()
				# 	with codecs.open('mafengwo_question_answer.txt','a+','utf-8') as f:
				# 		f.write('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+title[0]+'\t'+'0'+'\t'+tmp[0]+'\r\n')
				# 		f.close()


test()