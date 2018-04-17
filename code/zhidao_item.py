#!/usr/bin/env python
# coding=utf-8
# author=hades
# 日本旅游相关问题及答案的爬取
from bs4 import BeautifulSoup
import urllib 
import requests
from lxml import etree
import codecs

# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool

def getItem():
    global url
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}    #构造浏览器头信息

    with open('1.txt','r') as f:
    	for line in f.readlines():
    		url = line
	        response = requests.get(url,headers=header)   #获取数据
	        html = response.content.decode("gbk")    #解码
	        selector = etree.HTML(html)
	        links = selector.xpath('//a[@class="ti"]/@href')
	        for url in links:
	        	r = requests.get(url,headers=header)
	        	html = r.content.decode("gbk")
	        	selector = etree.HTML(html)
	        	question = selector.xpath('//span[@class="ask-title "]/text()')
	        	# question_detail = selector.xpath('//div[@class="line mt-5 q-content"]/span/text()')
	        	answer_bingo = selector.xpath('//div[@class="line content"]/text()')
	        	answer = selector.xpath('//div[@class="answer-text line"]/span/text()')
	        	# answer_img = selector.xpath('//div[@class="answer-text line"]/span/img/text()')
	        	answer_img = selector.xpath('//img[@class="word-replace"]')
	        	print answer_img
	        	if len(answer_img)==0:
	        		pass
	        	else:
	        	    for img in answer_img:
	        		   answer = img+answer
	        	with codecs.open('items.txt','a+','utf-8') as f :
	        		f.write(u'问题：'+question[0]+'\r')

		        	if len(answer_bingo)==0:
		        		f.write(u'最佳答案：'+u'无'+'\r')

		        	else:
		        	    f.write (u'最佳答案：'+answer_bingo[0]+'\r')

		        	if len(answer)==0:
		        		f.write(u'其他答案：'+u'无'+'\r')

		        	else:

		        	    f.write(u'其他答案：'+answer[0]+'\r')
		        	f.close()

	        	# print (u'问题：'+question[0]+'\n')
	        	# if len(answer_bingo)==0:
	        	# 	print(u'最佳答案：'+u'无')
	        	# else:
	        	#     print (u'最佳答案：'+answer_bingo[0]+'\n')
	        	# if len(answer)==0:
	        	# 	print(u'其他答案：'+u'无')
	        	# else:

	        	#     print (u'其他答案：'+answer[0]+'\n')


getItem()