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
import threadpool as tp
import re
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
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'tuniu_partner=MTAwLDAsLDI2OWJhMjJhNDAxOWQyNDRjYzNkMGU4ODZkMjQ1NGFk; connect.sid=s%3AwmXiJ9VeXhpmYWtNP4XU9XAVQe457J92.fE6iJoJ7X9%2BwbV8E1MIiO4jE%2BFN9jmmQgmI2Jo352s8; __utma=1.1367352016.1521080530.1521080530.1521080530.1; __utmc=1; __utmz=1.1521080530.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _tacau=MCwzOTM0MGU3NC01YTAzLWNiMjEtN2YyYS1lNWE1YTJkNDFhNjYs; _tact=MzFmNzM0NDUtYzE1NC05NzQyLWEwMDYtYTZjNDQ2YzE3ZWJl; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _taca=1521080530202.1521080530202.1521080530202.1; _tacb=ZDYzY2NmMjEtNWQ0Yi1jMDVmLTU2ZTUtM2ZkNDA3YmE4NzZh; _tacc=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1521080531; __utmb=1.4.10.1521080530; Hm_lpvt_51d49a7cda10d5dd86537755f081cc02=1521080567',
	'Host': 'www.tuniu.com',
	'If-None-Match': 'W/"112a0-UwD5Sztfcd9i/kN0cI1YYlZKQcE"',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
}

def test(xxxx):
	for i in range(300):
		url = 'http://www.tuniu.com/papi/wenda/index/searchQuestion?d={"poiId":"","key":"日本","pageSize":20,"pageNumber":'+str(i)+'}&c={"ct":100}&_=1521081102723'
		# response = requests.get(url,headers=headers,timeout=5,verify=False)
		while True:
			try:
				response = requests.get(url,headers=headers,timeout=20,verify=False)
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				break
			except:
				print('let us go  sleep!!!')
				sleep(20)
				print('ogo')
				continue

		json_data = json.loads(response.content)
		data = json_data['data']
		list_ = data['list']
		for link in list_:
			urls = json.dumps(link)
			urls = json.loads(urls)
			id_ = urls['questionId']
			with codecs.open('tuniu_ids.txt','a+','utf-8') as f :
				f.write(str(id_)+'\n')
				f.close()
				print(id_)
			print(urls['questionId'])
			url = 'http://www.tuniu.com/wenda/detail-' + str(urls['questionId'])

			# url = 'http://www.mafengwo.cn/wenda/detail-2630437.html'
			if url not in url_list:
				url_list.append(url)
				# r = requests.get(url,headers=headers,timeout=5)
				while True:
					try:
						r = requests.get(url,headers=headers,timeout=20,verify=False)
						requests.adapters.DEFAULT_RETRIES = 5
						s = requests.session()
						s.keep_alive = False
						break


					except:
						print('let us go  sleep!!!')
						sleep(20)
						print('ogo')
						continue	
				html = r.content.decode("utf-8")  # 解码
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				selector = etree.HTML(html)
				title = selector.xpath('//div[@class="title"]/h2/text()')
				if title == []:
					print(url)
				else:
					title =title[0]
				answers = selector.xpath('//li[@class="item clearfix J_answerItem"]'
										)
				desc = ''

				for answer in answers:
					answer_content = answer.xpath('./div[@class="col-2"]/div[@class="col-2-bd"]/p/text()')[0]
					like = answer.xpath('./div[@class="col-1"]/a/p/text()')[0]
					bingo = answer.xpath('./div[@class="col-2"]/div[@class="col-2-hd"]/div[@class="hd-col-2 clearfix"]/a[@class="act on"]')
					if bingo==[]:
						with codecs.open('tuniu_question_answer.txt','a+','utf-8') as f:
							if desc == '' :
		
							    s = ('1'+'\t'+'qid:'+str(id_)+'\t'+title+'\t'+answer_content+'\t'+'0'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
							    f.write(s+'\r\n')
							    f.close()
							else:
							    s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+answer_content+'\t'+'0'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
							    f.write(s+'\r\n')
							    f.close()
					else:
						with codecs.open('tuniu_question_answer.txt','a+','utf-8') as f:
							if desc == '' :
		
							    s = ('1'+'\t'+'qid:'+str(id_)+'\t'+title+'\t'+answer_content+'\t'+'1'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
							    f.write(s+'\r\n')
							    f.close()
							else:
							    s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+answer_content+'\t'+'1'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
							    f.write(s+'\r\n')
							    f.close()


args = ['xxxx','aaa','a']
pool = tp.ThreadPool(20)
reqs = tp.makeRequests(test, args)
[pool.putRequest(req) for req in reqs]
pool.wait