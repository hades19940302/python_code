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
import threadpool as tp
import re
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from requests.adapters import HTTPAdapter
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=['https://cn.oshiete.goo.ne.jp/qa/list?page=']
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
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
            h = re.sub(r'<br[ ]?/?>', '\n', h)
            selector = etree.HTML(h)
            question = selector.xpath('//h1[@class="articleQ_ttl"]/text()')[0]
            question_p = selector.xpath('//p[@class="articleQ_text"]')
            # question_h = selector.xpath('//*[@id="colLt"]/div/div[1]/div[1]/div[2]/div[1]/h1/text()')
            answer_h = selector.xpath('//ul[@class="listAnswer listQA"]/li/div[@class="list_detail"]/div[@class="list_text"]')
            about_questions = selector.xpath('//ul[@class="listQA inlineSP"]/li/a/div[@class="list_detail"]')

            print(about_questions)
            if question_p == []:
                desc = ''
            else:
                desc = question_p[0].xpath('string(.)').strip()
            for  about_question in about_questions:
                with codecs.open('oshiete_question_question.txt','a+','utf-8') as f1 :
                    if desc == '':
                        s = ('1'+'\t'+'qid:'+id_+'\t'+question+'\t'+about_question.xpath('./div[@class="list_ttl"]')[0].xpath('string(.)').strip()+'#'+about_question.xpath('./div[@class="list_text"]')[0].xpath('string(.)').strip()).strip().replace('\n','').replace('\r','')
                        f1.write(s+'\r\n')
                        f1.close()
                    else:
                        s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+about_question.xpath('./div[@class="list_ttl"]')[0].xpath('string(.)').strip()+'#'+about_question.xpath('./div[@class="list_text"]')[0].xpath('string(.)').strip()).strip().replace('\n','').replace('\r','')
                        f1.write(s+'\r\n')
                        f1.close()
            for answer in answer_h:
                print(answer)
                answer_desc = answer.xpath('./p')[0].xpath('string(.)').strip()
                title = answer.xpath('./h2/text()')[0]

                print(desc,title[0])
                with codecs.open('oshiete_question_answer.txt','a+','utf-8') as f:
                    if desc == '':
                        s = ('1'+'\t'+'qid:'+id_+'\t'+question+'\t'+title+desc+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
                        f.write(s+'\r\n')
                        f.close()
                    else:
                        s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+title+answer_desc+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
                        f.write(s+'\r\n')
                        f.close()

getNewUrlList()