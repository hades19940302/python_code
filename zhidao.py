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
import threadpool as tp
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
from requests.adapters import HTTPAdapter
from time import sleep
from urllib import quote
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',	
	'Connection': 'keep-alive',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
	}

header = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
topics = ['去日本旅游要多少钱','日本必去十大景点排名','日本旅游价格表跟团','去日本必买的东西','日本旅游攻略','日本购物必买清单','日本旅游多少钱','去日本旅游必买的东西','日本旅游价格',
	'日本好玩的地方排名榜','日本东京十大著名景点','日本著名景点有哪些','日本最值得去的地方','日本旅游景点排名','日本必游十大景点','日本东京景点介绍','东京必去的景点排行榜',
	'2017日本购物血拼清单','2017日本十大必买清单','日本购物必买清单','男人日本购物必买清单','日本购物必买清单100','日本购物男士必买清单','日本购物男士电子产品','日本购物必买清单女生','日本购物必买清单女生',
	'日本特色景点','日本著名景点','日本景点排名','日本著名旅游景点介绍','日本著名景点有哪些','去日本买什么最划算','去日本必买的东西','日本特色美食','日本特色景点介ppt',
	'日本旅行报价','日本自由行7天费用','日本旅行费用','日本旅行报价','日本旅行地方','日本旅行去哪里好','日本旅行最佳时间','去日本旅行要多少钱','日本旅行团报价',
	'日本人饮食一日三餐','日本饮食文化','古代日本饮食','日本饮食文化特点','关于日本饮食的书','日本人饮食结构','名古屋旅游必去景点','神户有什么好玩的吗','池袋附近有什么好玩的','和歌山有什么好玩的','神户有什么好玩的地方',
	'日本交通情况','日本交通app','日本交通特点','日本交通费用','日本交通贵吗','日本交通规则','日本东京交通攻略','奈良有什么好玩的地方','京都附近有什么好玩的','冬天京都有哪些好玩的','大阪有哪些好玩的地方','京都一日游最佳路线',
	'日本酒店贵吗','日本著名酒店','日本有名酒店','日本酒店有洗漱用品吗','日本东京酒店','日本东京五星级酒店','angsana酒店','日本攻略','名古屋有什么好玩的','日本奈良有什么好玩的','名古屋 好玩吗','关西有什么好玩的地方','名古屋和大阪哪个好玩',
	'日本旅游北海道自由行','日本攻略购物篇','日本旅游攻略 冬季','日本旅行攻略','日本攻略 自由行','大阪晚上好玩的地方','大阪附近好玩的地方','大阪附近有什么好玩的','大阪有啥好玩的地方','千叶有哪些好玩的地方','奈良有什么好玩的',
	'日本 奈良 鹿','日本永谷园','日本 必买 吃','去日本有历史的地方','东京有名的地方','东京必去的景点','东京哪些地方好玩','元旦到东京哪里好玩','大阪有哪些好玩的地方','东京购物去哪些地方好','京都有什么好玩的地方',
	'日本度假城市','日本特色建筑有哪些','日本最好玩的城市','日本最值得去的地方','日本关西包括哪些城市','日本哪个海港城市好玩','日本大阪周边城市','北海道必去的地方','日本的温泉哪里最好','日本值得去的旅游名胜','东京哪些地方值得去','日本必去的几大景点','日本有意义的地方',]


topics2 = []
def test(xxx):
	f =open('baiduzhidao_topics_list_1.txt','rb')
	for line in f.readlines():
		line = line.replace('\n','').replace('\r','').strip()
		if line not in topics2:
			topics2.append(line)
	for topic in topics2:
		for i in range(0,770,10):
			url = 'https://zhidao.baidu.com/search?word='+topic+'&pn='+str(i)
			while True:
				try:
					r = requests.get(url,headers=header,timeout=20,verify=False)
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					break


				except:
					print('let us go  sleep!!!')
					sleep(20)
					print('ogo')
					continue
			requests.adapters.DEFAULT_RETRIES = 5
			s = requests.session()
			s.keep_alive = False
			html = r.content # 解码
			html = re.sub(r'<br[ ]?/?>', '\n', html)
			selector = etree.HTML(html)
			links = selector.xpath('//dl[@class="dl"]/dt[@class="dt mb-4 line"]/a/@href')
			for link in links:
				# url = 'https://zhidao.baidu.com/question/1732180052597957147.html'
				link = link[:link.index('?fr')]
				print(link)
				with codecs.open('baiduzhidao_url_list_4.txt','a+','utf-8') as f :
						f.write(link+'\r\n')
						f.close()

topics_list = []
def test2(xxx):
	with open('baiduzhidao_topics_list_1.txt','rb') as f :
		for line in f.readlines():
			url = 'https://m.baidu.com/sf/vsearch?pd=wenda_tab&word='+quote(line)+'&tn=vsearch&sa=vs_tab&lid=6674709264707130762&ms=1&from=1012015a'
			response = requests.get(url,headers=headers,timeout=20,verify=False)
			requests.adapters.DEFAULT_RETRIES = 5
			s = requests.session()
			s.keep_alive = False
			html = response.content # 解码
			html = re.sub(r'<br[ ]?/?>', '\n', html)
			selector = etree.HTML(html)	
			topics = selector.xpath('//div[@class="c-result sfc-log"]/div/article/div/div/div')
			for topic in topics:
				topic = topic.xpath('string(.)').strip()
				if topic not in topics_list:
					topics_list.append(topic)
					with codecs.open('baiduzhidao_topics_list_1.txt','a+','utf-8') as f1:

						# f1 = open('baiduzhidao_topics_list.txt','a+')
						f1.write(topic+'\n')
						f1.close()

	f.close()


	print(topics)

topics_list_has = []
def test3(xx):
	f= open('baiduzhidao_topics_list_1.txt','rb')
	for line in f.readlines():
		line = line.replace('\n','').replace('\r','').strip()
		if line not in topics_list_has:
			topics_list_has.append(line)
			f1 = open('topics_list_has.txt','a+')
			f1.write(line+'\n')
			f1.close()
			print(line)

	f.close()
def test4(xx):
	with codecs.open('baiduzhidao_topics_list_1.txt','a+','utf-8') as f :
		for line in f.readlines():
			line = line.replace('\n','').replace('\r','').strip()
			if line not in topics_list_has:
				topics_list_has.append(line)
				with codecs.open('topics_list_has.txt','a+','utf-8') as f1:
					f1.write(line+'\n')
					f1.close()

	f.close()




args = ['xxxx','aa','aaa']
pool = tp.ThreadPool(10)
reqs = tp.makeRequests(test, args)
[pool.putRequest(req) for req in reqs]
pool.wait()
# test2()
