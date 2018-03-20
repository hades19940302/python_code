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
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
url_list=[]
id_list = []
rb = {}
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}  # 构造浏览器头信息
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Cookie': 'Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=61ba01de-17cd-4ee0-a4d8-a90718e4288e; MKT_Pagesource=PC; _ga=GA1.2.1600563002.1520911998; traceExt=campaign=CHNbaidu81&adid=index; _RF1=218.24.167.7; _RSG=xN4ghJMWN4CHO_5JJPx6BB; _RDG=28ae5734b11f6d2fde22ba0d23caf03836; _RGUID=c1178164-eba8-45fb-b2c6-ed94d317f611; bdshare_firstime=1520912009327; ASP.NET_SessionSvc=MTAuOC4xODkuNTZ8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUxMjA5MzU2NjE2OA; _gid=GA1.2.1039661798.1521083434; _gat=1; appFloatCnt=3; manualclose=1; _bfa=1.1520911993569.9mocz.1.1520911993569.1521083431281.2.6; _bfs=1.4; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1521083469782%7D%5D; _jzqco=%7C%7C%7C%7C1520912002269%7C1.726710025.1520911998566.1521083465814.1521083469804.1521083465814.1521083469804.0.0.0.6.6; __zpspc=9.2.1521083434.1521083469.4%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _bfi=p1%3D290104%26p2%3D290104%26v1%3D6%26v2%3D4',
	'Host': 'you.ctrip.com',
	'Referer': 'http://you.ctrip.com/asks/search/?keywords=%E6%97%A5%E6%9C%AC',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
}

def test():
	for i in range(5):
		url = 'http://you.ctrip.com/asks/search/p'+str(i)+'?keywords=%E6%97%A5%E6%9C%AC&type=1'
		response = requests.get(url,headers=headers,timeout=5,verify=False)
		html = response.content.decode('utf-8')
		selector = etree.HTML(html)
		links = selector.xpath('//li[@class="cf"]/@href')
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		s.keep_alive = False
		# links = selector.xpath('//h2[@class="ask_title"]/span/text()')
		for link in links:
			url = 'http://m.ctrip.com/html5/you'+link
			id_ = link[-12:-5]
			# url = 'http://www.mafengwo.cn/wenda/detail-2630437.html'
			if url not in url_list:
				url_list.append(url)
				header = {
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
					'Accept-Encoding': 'gzip, deflate',
					'Accept-Language': 'zh-CN,zh;q=0.9',
					'Connection': 'keep-alive',
					'Cookie': 'Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _abtest_userid=61ba01de-17cd-4ee0-a4d8-a90718e4288e; _ga=GA1.2.1600563002.1520911998; traceExt=campaign=CHNbaidu81&adid=index; _RF1=218.24.167.7; _RSG=xN4ghJMWN4CHO_5JJPx6BB; _RDG=28ae5734b11f6d2fde22ba0d23caf03836; _RGUID=c1178164-eba8-45fb-b2c6-ed94d317f611; appFloatCnt=3; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1521085315471%7D%5D; _bfs=1.1; _gid=GA1.2.1002920052.1521530718; __zpspc=9.3.1521530718.1521530718.1%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; ASP.NET_SessionSvc=MTAuMTUuMTI4LjMwfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTUwOTk3MjM0Mjc5Ng; MKT_Pagesource=H5; _fpacid=09031119411931292084; _jzqco=%7C%7C%7C%7C1520912002269%7C1.726710025.1520911998566.1521530718441.1521530719888.1521530718441.1521530719888.0.0.0.16.16; GUID=09031119411931292084; _bfa=1.1520911993569.9mocz.1.1521083431281.1521530720207.3.16.214073; _bfi=p1%3D290104%26p2%3D0%26v1%3D15%26v2%3D0',
					'Host': 'm.ctrip.com',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
					
				}
				r = requests.get(url,headers=header,timeout=5)
				html = r.content.decode("utf-8")  # 解码
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				selector = etree.HTML(html)
				title = selector.xpath('//div[@class="pnl_askInfo"]/div[@class="title"]/text()')
				desc = selector.xpath('//div[@class="summary replayContent"]/p/span/text()')
				if desc == []:
					desc = ''
				else:
					desc = desc[0]
				answers = selector.xpath('//li[@class="pnl_answerInfo"]')
				related_asks = selector.xpath('//div[@class="related_issues"]/ul/li/p/text()')
				for related_ask in related_asks:
					with codecs.open('ctrip_question_question.txt','a+','utf-8') as f:
						f.write('1'+'\t'+'qid:'+id_+'\t'+title[0]+'#'+desc+'\t'+related_ask+'\r\n')
						f.close()					
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				print(answers)
				if answers == []:
					pass
				else:
					for answer in answers:
						like = answer.xpath('./div[@class="prop"]/div[@class="common-iconfont control active"]/span/text()')
						answer_title = answer.xpath('./div[@class="title"]/text()')
						print(like,answer_title)
						if like == []:
							like = 0
						else:
							like = like[0]
						with codecs.open('ctrip_question_answer.txt','a+','utf-8') as f:
							f.write('1'+'\t'+'qid:'+id_+'\t'+title[0]+'#'+desc+'\t'+answer_title[0]+'\t'+'0'+'\t'+str(like)+'\r\n')
							f.close()

			else:
				pass

test()