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
	for i in range(2):
		url = 'http://www.mafengwo.cn/qa/ajax_qa/more?type=0&mddid=10183&tid=&sort=1&key=&page='+str(i)
		response = requests.get(url,headers=header,timeout=5,verify=False)

		json_data = json.loads(response.content)
		html = json_data['data']
		html = html['html']
		selector = etree.HTML(html)
		links = selector.xpath('//li[@class="item clearfix _j_question_item"]/div/div[@class="title"]/a/@href')
		for link in links:
			url = 'http://www.mafengwo.cn'+link
			if url not in url_list:
				url_list.append(url)
				r = requests.get(url,headers=header,timeout=5)
		        
				html = r.content.decode("utf-8")  # 解码
				selector = etree.HTML(html)
				title = selector.xpath('//div[@class="q-title"]/h1/text()')
				answers = selector.xpath('//div[@class="_j_answer_html"]/text()')
				for answer in answers:

					rb['答案'] = answer
					rb['问题'] = title
					rb['QID'] = link[14:22]
					rb['LIKE'] = 0
					rb['BEST'] = 0
					rb['IN'] = 1
					tmp = json.dumps(rb).replace(' ','')
					data = tmp.decode('unicode-escape')
					with codecs.open('mafengwo.txt','a+','utf-8') as f:
						f.write(str(data)+'\r\n')
						f.close()
			else:
				pass

test()