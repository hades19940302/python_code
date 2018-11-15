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
import threadpool as tp
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
url_list=[]
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
from requests.adapters import HTTPAdapter
from time  import sleep
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))


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

def test():
	f1 = open('tuniu_ids.txt','rb')
	i = 1
	for id_ in f1.readlines():
		id_ = id_.strip()
		r = requests.get('http://www.tuniu.com/papi/wenda/detail/answerList?d=%7B%22questionId%22%3A%22'+id_+'%22%2C%22pageSize%22%3A10%2C%22pageNumber%22%3A2%7D&c=%7B%22ct%22%3A100%7D&_=1522048749856',headers=headers,timeout=20,verify=False)
		json_data = json.loads(r.content)
		data = json_data['data']
		list_ = data['list']
		print(list_)
		if list_ == []:
			pass
		else:
			url_detail = 'http://www.tuniu.com/wenda/detail-' + str(id_)
			print(url_detail)

			# url = 'http://www.mafengwo.cn/wenda/detail-2630437.html'
			while True:
				try:
					r_2 = requests.get(url_detail,headers=headers,timeout=20,verify=False)
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					break


				except:
					print('let us go  sleep!!!')
					sleep(20)
					print('ogo')
					continue
			html = r_2.content.decode("utf-8")  # 解码
			html = re.sub(r'<br[ ]?/?>', '\n', html)
			selector = etree.HTML(html)
			title = selector.xpath('//div[@class="title"]/h2/text()')
			if title == []:
				pass

			else:
				title = title[0]
				print(title)
				for item in list_:
					answer = item['answer']
					print(answer)
					like = item['likes']
					s = ('1'+'\t'+'qid:'+str(id_)+'\t'+title+'\t'+answer+'\t'+'0'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
					with codecs.open('tuniu_question_answer.txt','a+','utf-8') as f:
						f.write(s+'\r\n')
						f.close()





test()



