#!/usr/bin/env python
# coding=utf-8
# author=hades
# 携程网日本相关信息爬取
import requests
from lxml import etree
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
ctrip_url = "http://m.ctrip.com"
url='http://m.ctrip.com/restapi/h5api/searchapp/search?action=autocomplete&source=globalonline&keyword=%E6%97%A5%E6%9C%AC&t=1520912506345'

def getItem():
    header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}    #构造浏览器头信息
    response=requests.get(url,headers=header)   #获取数据
    html=response.content.decode("gbk")    #解码
    selector=etree.HTML(html)
    last_link = selector.xpath('//a[@class="pager-last"]/@href')