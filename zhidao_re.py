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
answers2_list = []
from requests.adapters import HTTPAdapter
from time  import sleep
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Cookie': 'IKUT=9083; BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; locale=zh; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1521679018,1521700344,1521717685,1521723445; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1521624927,1521680045,1521700358,1521723528; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1521723528; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1521725708',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
	}

header = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'no-cache',
	'Cookie': 'IKUT=9083; BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; locale=zh; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1521679018,1521700344,1521717685,1521723445; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1521723445; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1521624927,1521680045,1521700358,1521723528; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1521723528',
	'Host': 'zhidao.baidu.com',
	'Pragma': 'no-cache',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
	
	}

def test():
	f1 = open('baiduzhidao_url_list.txt','rb')
	for url in f1.readlines():
		id_ = url[34:-7]
		if id_ not in id_list:
			id_list.append(id_)
			while True:
				try:
					r = requests.get(url,headers=headers,timeout=50,verify=False)
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					break


				except:
					print('let us go  sleep!!!')
					sleep(5)
					print('ogo')
					continue	
			html = r.content.decode("utf-8")  # 解码
			html = re.sub(r'<br[ ]?/?>', '\n', html)
			selector = etree.HTML(html)
			best_wgt = selector.xpath('//div[starts-with(@class,"wgt-best")]')

			answer_best = selector.xpath('//div[@class="w-reply-container w-reply-item-quality"]/div[@class="w-detail-full"]/div[@class="w-detail-container w-detail-1"]/div/div')
			like = selector.xpath('//div[@class="w-reply-container w-reply-item-quality"]/div[@class="append"]/div/div[@class="question-meta-support question-meta-support-area"]/span/@data-support')
			question = selector.xpath('//div[@class="wgt-question-title"]/h2')[0]
			question_desc = selector.xpath('//div[@class="wgt-question-meta"]/div/div[@class="wgt-question-desc"]/div')
			bingo = selector.xpath('//div[@class="best-answer-icon"]')
			r_question_list_titles  = selector.xpath('//div[@class="w-question-list"]/a/span')

			if question_desc == []:
				desc = ''
			else:
				desc = question_desc[0].xpath('string(.)').strip()
			if like == []:
				pass
			else:
				if bingo == []:
					with codecs.open('zhidao_question_to_answer_re.txt','a+','utf-8') as f:
						# f.write(str(data)+'\r\n')
							if desc == '':
								s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'\t'+answer_best[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
								f.write(s+'\r\n')
								f.close()
								print('ok')
							else:
								s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+answer_best[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
								f.write(s+'\r\n')
								f.close()
								print('ok')

				else:

					with codecs.open('zhidao_question_to_answer_re.txt','a+','utf-8') as f:
						# f.write(str(data)+'\r\n')
							if desc == '':
								s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'\t'+answer_best[0].xpath('string(.)').strip()+'\t'+'1'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
								f.write(s+'\r\n')
								f.close()
								print('ok')
							else:
								s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+answer_best[0].xpath('string(.)').strip()+'\t'+'1'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
								f.write(s+'\r\n')
								f.close()
								print('ok')
							for r_question_list_title in r_question_list_titles:

				with codecs.open('zhidao_question_to_question_1.txt','a+','utf-8') as f1:
					if desc == '':
						s = ('1'+'\t'+'qid:'+str(id_)+'\t'+question.xpath('string(.)').strip()+'\t'+r_question_list_title.xpath('string(.)').strip()).strip().replace('\n','').replace('\r','')
						f1.write(s+'\r\n')
						f1.close()
						print('ok')
					else:
						s = ('1'+'\t'+'qid:'+str(id_)+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+r_question_list_title.xpath('string(.)').strip()).strip().replace('\n','').replace('\r','')
						f1.write(s+'\r\n')
						f1.close()
						print('ok')