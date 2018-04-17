#!/usr/bin/env python
# coding=utf-8
# author=hades
# 百度知道手机端日本旅游相关问题爬取
import urllib 
import requests
from lxml import etree
import codecs
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
zhidao_url = "https://zhidao.baidu.com"
start_url='https://m.baidu.com/sf/vsearch?pd=wenda_tab&word=%E6%97%A5%E6%9C%AC%E6%97%85%E6%B8%B8&tn=vsearch&sa=vs_tab&lid=10901393999300164688&ms=1'
index_word = start_url.index('word')
index_tn = start_url.index('tn')
def getRelevant():
    global start_url
    header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}    #构造浏览器头信息
    response=requests.get(start_url,headers=header)   #获取数据
    html=response.content.decode("utf-8")    #解码
    selector=etree.HTML(html)
    relevant_topics = selector.xpath('//a[@class="c-gap-top-small c-gap-bottom-small c-blocka c-slink-new-strong"]/span/text()')
    topic =  start_url[(index_word+5):(index_tn-1)]
    topic = urllib.unquote(topic)

    for topics in relevant_topics:
    	# topic = urllib.quote(topics)
    	url = start_url[:index_word+5]+topics+start_url[index_tn-1:]
    	m_index = url.index('m')
    	url = url[:m_index]+"www"+url[(m_index+1):]
    	r = requests.get(url,headers=header)
    	# print topics
    	with codecs.open('answer_answer.txt','a+','utf-8') as f :
    		print topic,topics
    		f.write(u'问题：'+topics+' ')
    		f.write(u'相关问题：'+topics+'\r')
    		f.close()


    # print topic
    # while True:

    # 	pass



    # contents = selector.xpath('//div[@id="content_right"]/div[@class="content_list"]/ul/li[div]')    使用xpath语法解析获取数据//表示从根开始查找@后跟相应的html属性
    # for eachlink in contents:
    #     url = eachlink.xpath('div/a/@href')[0] if str(eachlink.xpath('div/a/@href')[0]).__contains__("http") else "http://www.chinanews.com"+eachlink.xpath('div/a/@href')[0]
    #     title = eachlink.xpath('div/a/text()')[0]
    #     ptime = eachlink.xpath('div[@class="dd_time"]/text()')[0]
    #     yield (title,url,ptime)




getRelevant()