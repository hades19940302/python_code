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

def test():
	for i in range(15):
		url = 'https://zhidao.baidu.com/msearch/ajax/getsearchlist?word=%E6%97%A5%E6%9C%AC%E6%97%85%E6%B8%B8&pn='+str(i)
		response = requests.get(url,headers=headers,timeout=20,verify=False)

		json_data = json.loads(response.content)
		data = json_data['data']
		entry = data['entry']
		for en in entry:
			# url = 'https://zhidao.baidu.com/question/1732180052597957147.html'
			en = json.dumps(en)
			en = json.loads(en)
			url = 'https://zhidao.baidu.com'+en['url']
			if url not in url_list:
				url_list.append(url)
				r = requests.get(url,headers=headers,timeout=5)
		        
				html = r.content.decode("utf-8")  # 解码
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				selector = etree.HTML(html)
				title = selector.xpath('//div[@class="wgt-question-title"]/h2/text()')
				answers = selector.xpath('//div[@class="full-content"]/text()')
				like = selector.xpath('//span[@class="js-question-meta-num question-meta-support-num"]/text()')
				if len(answers)==0:
					pass
				else:
					for answer in answers:
						rb['答案'] = answer
						rb['问题'] = title
						rb['QID'] = en['url'][10:-5]
						rb['LIKE'] = like
						rb['BEST'] = 1
						rb['IN'] = 1
						tmp = json.dumps(rb).replace(' ','')
						data = tmp.decode('unicode-escape')
						with codecs.open('zhidao2.txt','a+','utf-8') as f:
							f.write(str(data)+'\r\n\t')
							f.close()

				print(data)
			else:
				pass

test()