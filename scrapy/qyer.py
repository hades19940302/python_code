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
reload(sys)
sys.setdefaultencoding( "utf-8" )
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
url_list=[]
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
rb = {}
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Cookie': '_guid=R235046d-c351-7518-8e2b-da9c5c7e8cd9; new_uv=1; PHPSESSID=6426bc4605987330f92854c4ea527559; __utma=253397513.1465259844.1521095861.1521095861.1521095861.1; __utmc=253397513; __utmz=253397513.1521095861.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); new_session=0; session_time=; init_refer=; als=0; isnew=1521095868361; __utmt=1; __utmb=253397513.7.10.1521095861',
	'Host': 'bbs.qyer.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
		}

def test():
	for i in range(1,5):
		url = 'http://bbs.qyer.com/forum-57-5-'+str(i)+'.html'
		response = requests.get(url,headers=headers,timeout=50,verify=False)
		html = response.content.decode('utf-8')
		selector = etree.HTML(html)
		links = selector.xpath('//dt[@class="title fontYaHei"]/a/@href')
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		s.keep_alive = False
		for link in links:
			# url = 'http://ask.qyer.com/question/3387775.html'
			id_ = link[24:-5]
			url = 'http://m.qyer.com/ask/'+link[15:]
			if url not in url_list:
				url_list.append(url)
				header_mobile = {
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
					'Accept-Encoding': 'gzip, deflate',
					'Accept-Language': 'zh-CN,zh;q=0.9',
					'Cache-Control': 'max-age=0',
					'Connection': 'keep-alive',
					'Cookie': '_guid=R21a0462-78a9-d55b-3648-fbca346e3d27; __utmz=253397513.1521094067.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); isnew=1521094075373; als=0; __utma=253397513.1530515317.1521094067.1521427592.1521526278.4; __utmc=253397513; __utmt=1; session_time=1521526278.129; init_refer=; new_uv=4; new_session=0; __utmb=253397513.3.10.1521526278',
					'Host': 'm.qyer.com',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
				}
				r = requests.get(url,headers=header_mobile,timeout=50)
				print(r.status_code)		        
				html = r.content.decode("utf-8")  # 解码
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				selector = etree.HTML(html)
				question  = selector.xpath('//section[@class="askQuestion"]/h3')[0].xpath('string(.)').strip()
				desc = selector.xpath('//section[@class="askQuestion"]/article')[0].xpath('string(.)').strip()	
				answers = selector.xpath('//div[@class="askAnswer__box"]')
				about_questions = selector.xpath('//dl[@class="about-question"]/dd/a/text()')
				for about_question in about_questions:
					with codecs.open('qyer_question_question.txt','a+','utf-8') as f1:
						if desc == '':
							s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+'\t'+about_question).strip().replace('\n','').replace('\r','')
							f1.write(s+'\r\n')
							f1.close()
						else:
							s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+about_question).strip().replace('\n','').replace('\r','')
							f1.write(s+'\r\n')
							f1.close()			
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				if answers == []:
					pass

				else:
					for answer in answers:
						title = answer.xpath('./article/text()')[0]
						tmp = answer.xpath('./div[@class="askAnswer__box__revert"]/span[@class="support js-support"]/text()')
						like = tmp[0]
						with codecs.open('qyer_question_answer.txt','a+','utf-8') as f:
							if desc == '':
								s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+'\t'+title+'\t'+'0'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
								f.write(s+'\r\n')
								f.close()
							else:
								s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+title+'\t'+'0'+'\t'+str(like)).strip().replace('\n','').replace('\r','')
								f.write(s+'\r\n')
								f.close()
test()