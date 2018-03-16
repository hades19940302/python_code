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
		# urk = 'https://m.mafengwo.cn/wenda/ajax_qa/more?type=3&mddid=10183&tid=&sort=4&key=&page=1'
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
			url = 'https://m.mafengwo.cn'+link
			print(url)
			# url = 'http://www.mafengwo.cn/wenda/detail-9196334.html'
			if url not in url_list:
				url_list.append(url)
				headers = {

					'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
				}
				r = requests.get(url,headers=headers,timeout=5,verify=False)
		        
				html = r.content.decode("utf-8")  # 解码
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				selector = etree.HTML(html)
				title = selector.xpath('//div[@class="container no-padding"]/div[@class="q-detail"]/h3/text()')
				answers = selector.xpath('//div[@class="expandable"]/p/text()')
				likes = selector.xpath('//a[@class="btn-ding _j_vote on"]/b/text()')
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				if len(answers)==0:
					pass
				else:
					for answer in answers:
						print(answer)
						rb['答案'] = answer
						rb['问题'] = title
						rb['QID'] = link[14:22]
						try:
							rb['LIKE'] = likes[answers.index(answer)]
						except Exception as e:
							rb['LIKE'] = 0
						rb['BEST'] = 0
						rb['IN'] = 1
						tmp = json.dumps(rb).replace(' ','')
						data = tmp.decode('unicode-escape')
						with codecs.open('mafengwo2.txt','a+','utf-8') as f:
							f.write(str(data)+'\r\n')
							f.close()

				print(data)
			else:
				print('else')

test()