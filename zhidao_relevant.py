#!/usr/bin/env python
# coding=utf-8
# author=hades
# 日本旅游相关问题的爬取
from bs4 import BeautifulSoup
import urllib 
import requests
from lxml import etree
import jieba  
from selenium import webdriver

# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
zhidao_url = "https://zhidao.baidu.com"
url='https://zhidao.baidu.com/search?word=%C8%D5%B1%BE%C2%C3%D3%CE&ie=gbk&site=-1&sites=0&date=0&pn=0'

def getRelevant():
    global url
    header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}    #构造浏览器头信息
    response=requests.get(url,headers=header)   #获取数据
    html=response.content.decode("gbk")    #解码
    browser = webdriver.Chrome()
    browser.get(url)
    browser.switch_to_frame('_bdrec_iframe_')
    span = browser.find_elements_by_css_selector('span[class="c-span4 c-line-clamp1 rw-item"]/a/text()')
    print span 
	# print('专辑名字：', browser.find_element_by_class_name('f-ff2').text)
	# for each in browser.find_elements_by_css_selector('a[href^=\/song]'):
	#     print("歌曲名字：",each.text)

    selector=etree.HTML(html)
    relevant_topics = selector.xpath('//div[@id="bdrecContainer"]/iframe/@src')
    print relevant_topics,type(relevant_topics)


getRelevant()