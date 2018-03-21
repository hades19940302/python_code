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
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}  # 构造浏览器头信息


def test():
	for i in range(1):
		url = 'http://www.mafengwo.cn/qa/ajax_qa/more?type=3&mddid=10183&tid=&sort=9&key=&page=0&time=2018-03-19+20%3A44%3A54'
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
				related_url = 'https://m.mafengwo.cn'+link
				related_r = requests.get(url,headers=header,timeout=5,verify=False)
		        
				html_r = related_r.content.decode("utf-8")  # 解码
				html_r = re.sub(r'<br[ ]?/?>', '\n', html_r)
				selector_r = etree.HTML(html_r)
				related_qts = selector_r.xpath('//div[@class="info"]/h3/text()')
				print(len(related_qts))
				if desc == []:
					desc = ''
				else:
					desc = desc[0]				

				for related_qt in related_qts :
					if desc == '':
						s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+'\t'+related_qt).strip().replace('\n','').replace('\r','')
						f1.write(s+'\r\n')
						f1.close()
					else:
						s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+related_qt).strip().replace('\n','').replace('\r','')
						f1.write(s+'\r\n')
						f1.close()					

				answers = selector.xpath('//li[starts-with(@class,"answer-item")]')
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				for  answer in answers:
					answer_content = answer.xpath('./div[@class="answer-content _js_answer_content"]/div[@class="_j_long_answer_item"]/div[@class="_j_answer_html"]')[0].xpath('string(.)').strip()
					like = answer.xpath('./div[@class="answer-side _js_answerAva"]/a/span/text()')[0]
					with codecs.open('mafengwo_question_answer.txt','a+','utf-8') as f:
						if desc == '':
							s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+'\t'+answer_content+'\t'+'0'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
							f.write(s+'\r\n')
							f.close()
						else:
							s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+answer_content+'\t'+'0'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
							f.write(s+'\r\n')
							f.close()

test()