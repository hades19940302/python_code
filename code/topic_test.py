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
topics = ['xxx']
def test():
	url = 'https://m.baidu.com/recsys/ui/api/rs?query='+topic+'&title='+topic+'&url=https%3A%2F%2Fzhidao.baidu.com%2Fsearch%3Fct%3D17%26pn%3D0%26tn%3Dikaslist%26rn%3D10%26fr%3Dwwwt%26word='+topic+'&ak=ZQ4m31EXvKem1HPYzaK8Ekq6opqfhKFK&pc=1&charset=gbk&contentTitleText=%C8%A5%CD%F8%D2%B3%CB%D1%CB%F7&entityNum=9'
	requests.get()
