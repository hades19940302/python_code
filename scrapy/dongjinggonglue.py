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
sys.setdefaultencoding("utf-8")
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list = []
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
rb = {}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}  # 构造浏览器头信息

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'dong_u_track=218.24.167.7.1521098849123101; Hm_lvt_c633c8754360ad7e8ffcc8557eac684f=1521098849,1521161048; Hm_lpvt_c633c8754360ad7e8ffcc8557eac684f=1521169070',
	'Host': 'www.dongjinggonglue.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
}

ids = []
for i in range(16):
  ids.append(i)
def test():
    for i in range(2):
        url = 'http://www.dongjinggonglue.com/zhinan/wenda/' 
        response = requests.get(url, headers=headers, timeout=20, verify=False)
        html = response.content.decode('utf-8')
        html = re.sub(r'<br[ ]?/?>', '\n', html)
        selector = etree.HTML(html)
        dts = selector.xpath('//dl[@class="qaList01 toggleBox01"]/dt/a/text()')
        dds =selector.xpath('//dl[@class="qaList01 toggleBox01"]/dd/text()')
        for dt in dts:

          id_ = ids.pop()
          with codecs.open('dongjinggonglue_question_answer.txt', 'a+', 'utf-8') as f:
              s = ('1'+'\t'+'qid:'+str(id_)+'\t'+dt+'\t'+dds[dts.index(dt)]+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
              f.write(s+'\r\n')
              f.close()

test()