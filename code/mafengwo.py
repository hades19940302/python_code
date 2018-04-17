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
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
id_list = []
rb = {}
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}  # 构造浏览器头信息
headers = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Cookie': 'mfw_uuid=5aa7464c-7a14-06bc-6770-bd3d89ea093c; _r=baidu; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A18%3A%22www.baidu.com%2Flink%22%3Bs%3A1%3A%22t%22%3Bi%3A1520911948%3B%7D; oad_n=a%3A5%3A%7Bs%3A5%3A%22refer%22%3Bs%3A21%3A%22https%3A%2F%2Fwww.baidu.com%22%3Bs%3A2%3A%22hp%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A3%3A%22oid%22%3Bi%3A1026%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222018-03-13+11%3A32%3A28%22%3B%7D; uva=s%3A264%3A%22a%3A4%3A%7Bs%3A13%3A%22host_pre_time%22%3Bs%3A10%3A%222018-03-13%22%3Bs%3A2%3A%22lt%22%3Bi%3A1520911957%3Bs%3A10%3A%22last_refer%22%3Bs%3A137%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DO7T8RXNSjfX-uEi2ZRImKEmxDZicWp3g92aOFeLBW_yoSYDcW2bQPbPda6MbWMt9%26wd%3D%26eqid%3De708cd5e000260ed000000025aa7464a%22%3Bs%3A5%3A%22rhost%22%3Bs%3A13%3A%22www.baidu.com%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1520911957%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5aa7464c-7a14-06bc-6770-bd3d89ea093c; UM_distinctid=1621d6aa1d5167-08e592f80cee9f-444a012d-15f900-1621d6aa1d64f1; PHPSESSID=cem19nk0rkrhr4e52hj958ae63; __mfwlv=1521076432; __mfwvn=4; CNZZDATA30065558=cnzz_eid%3D1554360833-1520911168-http%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1521076403; __mfwlt=1521076951',
	'Host': 'www.mafengwo.cn',
	'Referer': 'http://www.mafengwo.cn/wenda/area-10183.html',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
}

def test():
	for i in range(639):
		url = 'http://www.mafengwo.cn/qa/ajax_qa/more?type=0&mddid=10183&tid=&sort=1&key=&page='+str(i)+'&time=2018-03-15+10%3A06%3A24'
		response = requests.get(url,headers=headers,timeout=5,verify=False)
		json_data = json.loads(response.content)
		html = json_data['data']
		html = html['html']
		selector = etree.HTML(html)
		links = selector.xpath('//li[@class="item clearfix _j_question_item"]/div/div[@class="title"]/a/@href')
		for link in links:
			url = 'http://www.mafengwo.cn'+link
			# url = 'http://www.mafengwo.cn/wenda/detail-2630437.html'
			if url not in url_list:
				url_list.append(url)
				r = requests.get(url,headers=headers,timeout=5)
		        
				html = r.content.decode("utf-8")  # 解码
				selector = etree.HTML(html)
				title = selector.xpath('//div[@class="q-title"]/h1/text()')
				# answers = selector.xpath('//div[@class="_j_answer_html"]/text()')
				answers = selector.xpath('//div[@class="answer-content _js_answer_content"]/div[@class="_j_long_answer_item"]/div[@class="_j_answer_html"]/text()'
										)
				likes = selector.xpath('//a[@class="btn-ding _js_zan "]/span/text()')
				if len(answers)==0:
					rb['答案']='尚未有人回答此问题'
					# rb['答案'] = answer
					rb['问题'] = title
					rb['QID'] = link[14:22]
					rb['LIKE'] = 0
					rb['BEST'] = 0
					rb['IN'] = 1
					tmp = json.dumps(rb).replace(' ', '')
					data = tmp.decode('unicode-escape')
					with codecs.open('mafengwo.json', 'a+', 'utf-8') as f:
						f.write(str(data) + '\r\n')
						f.close()
				else:

					for answer in answers:
						rb['答案'] = answer
						rb['问题'] = title
						rb['QID'] = link[14:22]
						rb['LIKE'] = likes[random.choice(range(len(likes)))]
						rb['BEST'] = 0
						rb['IN'] = 1
						tmp = json.dumps(rb).replace(' ','')
						data = tmp.decode('unicode-escape')
						with codecs.open('mafengwo.json','a+','utf-8') as f:
							f.write(str(data)+'\r\n')
							f.close()
			else:
				pass

test()