#!/usr/bin/env python
# coding=utf-8
# author=hades
# 日本旅游详细页面URL的爬取
from bs4 import BeautifulSoup
import urllib 
import requests
from lxml import etree
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
zhidao_url = "https://zhidao.baidu.com"
url='https://zhidao.baidu.com/search?word=%C8%D5%B1%BE%C2%C3%D3%CE&ie=gbk&site=-1&sites=0&date=0&pn=0'

def getNewUrlList():
    global url
    header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}    #构造浏览器头信息
    response=requests.get(url,headers=header)   #获取数据
    html=response.content.decode("gbk")    #解码
    selector=etree.HTML(html)
    last_link = selector.xpath('//a[@class="pager-last"]/@href')
    tmp = last_link[0]
    zhidao_last = zhidao_url+tmp
    print zhidao_last
    r = requests.get(zhidao_last)
    r.encoding='gbk' 
    # print r.text
    index = zhidao_last.index('pn')
    length = len(zhidao_last)
    last_int = int(zhidao_last[95:])
    while True:
    	flag = last_int-10
    	if flag>=0:
    		url = 'https://zhidao.baidu.com/search?word=%C8%D5%B1%BE%C2%C3%D3%CE&ie=gbk&site=-1&sites=0&date=0&pn='+str(flag)
    		url_list.append(url)
    		last_int = flag
    		with open('1.txt','a+') as f:
    			f.write(url+'\n')
    			f.close()
    	else:
    		break

    print url_list


    # contents = selector.xpath('//div[@id="content_right"]/div[@class="content_list"]/ul/li[div]')    使用xpath语法解析获取数据//表示从根开始查找@后跟相应的html属性
    # for eachlink in contents:
    #     url = eachlink.xpath('div/a/@href')[0] if str(eachlink.xpath('div/a/@href')[0]).__contains__("http") else "http://www.chinanews.com"+eachlink.xpath('div/a/@href')[0]
    #     title = eachlink.xpath('div/a/text()')[0]
    #     ptime = eachlink.xpath('div[@class="dd_time"]/text()')[0]
    #     yield (title,url,ptime)




getNewUrlList()