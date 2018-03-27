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
url_list=[]
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
from requests.adapters import HTTPAdapter
from time  import sleep
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Cookie': 'BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; IKUT=2933; PSINO=2; BDRCVFR[rzhiDDnzJ-0]=mbxnW11j9Dfmh7GuZR8mvqV; H_PS_PSSID=; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1522026618,1522030814,1522030840,1522030980; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1522034895,1522034940,1522034988,1522038758; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1522040920; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1522041185',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
	}

def test(xx):
	while True:
			while True:
				try:
					r = requests.get('https://zhidao.baidu.com/question/91145209.html',headers=headers,timeout=20,verify=False)
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					break


				except:
					print('let us go  sleep!!!')
					sleep(20)
					print('ogo')
					continue	
				print(r)



args = ['xxxx','aaa','a']
pool = tp.ThreadPool(20)
reqs = tp.makeRequests(test, args)
[pool.putRequest(req) for req in reqs]
pool.wait()
		