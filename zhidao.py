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
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))

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

header = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Cookie': 'BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; IKUT=2933; H_PS_PSSID=1446_21101_22158; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1521979881,1521983621,1522026279,1522026618; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1522026726; PSINO=2; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1522026240,1522026245,1522026611,1522027070; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1522027343; PMS_JT=%28%7B%22s%22%3A1522027345835%2C%22r%22%3A%22https%3A//zhidao.baidu.com/search%3Fword%3D%25C8%25D5%25B1%25BE%25B1%25D8%25C8%25A5%25CA%25AE%25B4%25F3%25BE%25B0%25B5%25E3%25C5%25C5%25C3%25FB%26ie%3Dgbk%26site%3D-1%26sites%3D0%26date%3D4%26pn%3D750%22%7D%29',
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
def test(xxx):
	for topic in topics:
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
				with codecs.open('baiduzhidao_url_list_3.txt','a+','utf-8') as f :
						f.write(link+'\r\n')
						f.close()
args = ['xxxx']
pool = tp.ThreadPool(20)
reqs = tp.makeRequests(test, args)
[pool.putRequest(req) for req in reqs]
pool.wait()
		
