#!/usr/bin/env python
# coding=utf-8
# author=hades
# oshiete urls
from __future__ import print_function
from bs4 import BeautifulSoup
import urllib 
import requests
from lxml import etree
import json
import codecs
import sys
import re
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=['https://cn.oshiete.goo.ne.jp/qa/list?page=']
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
rb = {}
def getNewUrlList():
    header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}    #构造浏览器头信息

    for i in range(1,6):
        url = 'https://cn.oshiete.goo.ne.jp/qa/list?page='+str(i)
        response=requests.get(url,headers=header,verify=False)   #获取数据
        html=response.content.decode("utf-8")    #解码
        selector=etree.HTML(html)
        links = selector.xpath('//ul[@class="listQA"]/li/a[@class="linkBlock"]/@href')
        for link in links:
            id_ = link[4:]
            if id not in id_list:
                id_list.append(id)
            link = 'https://cn.oshiete.goo.ne.jp'+link
            url_list.append(link)
            r = requests.get(link,headers=header,verify=False,timeout=5)
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            h = r.content.decode('utf-8')
            html = re.sub(r'<br[ ]?/?>', '\n', html)
            selector = etree.HTML(h)
            question_h = selector.xpath('//h1[@class="articleQ_ttl"]/text()')
            question_p = selector.xpath('//p[@class="articleQ_text"]/text()')
            answer_h = selector.xpath('//ul[@class="listAnswer listQA"]/li/div[@class="list_detail"]/div[@class="list_text"]/h2/text()')
            answer_p = selector.xpath('//ul[@class="listAnswer listQA"]/li/div[@class="list_detail"]/div[@class="list_text"]/p/text()')
            answer_a = selector.xpath('//ul[@class="listAnswer listQA"]/li/div[@class="list_detail"]/div[@class="list_text"]/p/a/text()')

            for answer in answer_h:
                rb['问题'] = question_h
                try:
                    rb['答案'] = answer + answer_p[answer_h.index(answer)]
                except Exception:
                    rb['答案'] = answer           
                rb['正例'] = 1
                rb['QID'] = id_
                rb['是否最佳'] = 0
                rb['点赞'] = 0

            # if len(answer_h)==0 :
            #     if len(answer_p)==0:
            #         if len(answer_a)==0:
            #             json_data['答案']='无'

            #         else:
            #             json_data['答案'] = answer_a[i]

            #     else:
            #         json_data['答案'] = answer_p[i]
            # else:
            #     for i in range(len(answer_h)):
            #         json_data['答案'] = answer_h[i]
                tmp = json.dumps(rb)
                data = json.loads(tmp)
                json_data = tmp.decode('unicode-escape')
                with codecs.open('oshiete3.txt','a+','utf-8') as f:
                    f.write(str(json_data)+'\r\n')
                    f.close()


getNewUrlList()