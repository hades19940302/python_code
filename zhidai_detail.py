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

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=5))
s.mount('https://', HTTPAdapter(max_retries=5))

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1446_21101_22158; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1521090106; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1521090106; PSINO=2; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1521090535; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1521090535',
	'Host': 'zhidao.baidu.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
	}

def test():
	f1 = open('baiduzhidao_url_list.txt','rb')
	for url in f1.readlines():
		id_ = url[34:-7]

		# id_ = '984489770420233819'
		# url = 'https://zhidao.baidu.com/question/984489770420233819.html'
		
		if id_ not in id_list:
			id_list.append(id)
			while True:
				try:

					r = requests.get(url,headers=headers,timeout=50,verify=False)
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					print(id_)
					break


				except:
					print('let us go  sleep!!!')
					sleep(5)
					print('ogo')
					continue	
			html = r.content.decode("utf-8")  # 解码
			html = re.sub(r'<br[ ]?/?>', '\n', html)
			selector = etree.HTML(html)
			question = selector.xpath('//div[@class="wgt-question-title"]/h2/text()')[0]
			question_desc = selector.xpath('//div[@class="wgt-question-desc-inner"]/text()')
			r_question_list_titles  = selector.xpath('//span[@class="r-question-list-title "]/text()')

			if question_desc == []:
				desc = ''
			else:
				desc = question_desc[0]

			for r_question_list_title in r_question_list_titles:

				with codecs.open('zhidao_question_to_question.txt','a+','utf-8') as f1:
					try:
						if desc == '':
							s = ('1'+'\t'+'qid:'+str(id_)+'\t'+question+'#'+'\t'+r_question_list_title).strip().replace('\n','').replace('\r','')
							f1.write(s+'\r\n')
							f1.close()
						else:
							s = ('1'+'\t'+'qid:'+str(id_)+'\t'+question+'#'+desc+'\t'+r_question_list_title).strip().replace('\n','').replace('\r','')
							f1.write(s+'\r\n')
							f1.close()
					except Exception as e:
						print(id_)

			answers = selector.xpath('//div[starts-with(@class,"w-reply-item")]')
			bingo = selector.xpath('//div[@class="best-answer-icon"]')
			if len(answers)==0:
				pass
			else:
				for answer1 in answers:
					tmp = answer1.xpath('./div/div[starts-with(@class,"append")]/div/div')[3].xpath('./span/@data-support')[0]
					title = answer1.xpath('./div/div[@class="w-detail-full"]')[0].xpath('./div/div')[0].xpath('string(.)').strip()
					if tmp == 0  or tmp=='0':
						print('tmp出问题了'+id_)
					else:
						like = tmp
						if len(bingo)==0:
							right = str(0)
						else:
							right = str(1)
						with codecs.open('zhidao_question_to_answer.txt','a+','utf-8') as f:
								if desc == '':
									s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+'\t'+title+'\t'+right+'\t'+str(like)).strip().replace('\n','').replace('\r','')
									f.write(s+'\r\n')
									f.close()
								else:
									s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+title+'\t'+right+'\t'+str(like)).strip().replace('\n','').replace('\r','')
									f.write(s+'\r\n')
									f.close()				
			for i in range(5):


				r2_url = 'https://zhidao.baidu.com/mobile/replies?rn=6&new=1&hasLoadArgue=0&qid='+id_+'&samp_hit=246&pn='+str(i)+'&deleteArgue=0'
				headers2 = {
					'Host': 'zhidao.baidu.com',
					'X-Requested-With': 'XMLHttpRequest',
					'Accept-Language': 'zh-cn',
					'Accept-Encoding': 'br, gzip, deflate',
					'Cookie': 'IKUT=72; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1521689257; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1521516481,1521545561,1521593514,1521680877; BAIDUID=63A79D6D7BB65B2E5F7AA62621BF1CE0:FG=1; BIDUPSID=C67D3BC1B35B88999BED0DF9FA2EF8D7',
					'Connection': 'keep-alive',
					'Accept': '*/*',
					'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D60 Safari/604.1',
					# 'Referer': url,
				}
				while True:
					try:
						r2 = requests.get(r2_url,headers=headers2,timeout=50,verify=False)
						requests.adapters.DEFAULT_RETRIES = 5
						s = requests.session()
						s.keep_alive = False


						break
					except:
						print('let us go  sleep!!!')
						sleep(5)
						print('ogo')
						continue
					
				html2 = r2.content.decode("utf-8")  # 解码
				html2 = re.sub(r'<br[ ]?/?>', '\n', html2)
				selector2 = etree.HTML(html2)
				if selector2 == '' or selector2 == None:
					pass
				else:
					answers2 = selector2.xpath('//div[starts-with(@class,"w-reply-item")]')
					bingo2 = selector2.xpath('//div[@class="best-answer-icon"]')
					if answers2 == [] :
						pass
					else:
						for answer2 in answers2:

							tmp = answer2.xpath('./div/div[starts-with(@class,"append")]/div/div')[3].xpath('./span/@data-support')[0]
							title = answer2.xpath('./div/div[@class="w-detail-full"]')[0].xpath('./div/div')[0].xpath('string(.)').strip()
							if title not in answers2_list:
								print(tmp)
								answers2_list.append(title)
								if tmp==0  or tmp == '0':
									pass
								else:
									like = tmp
									if len(bingo2)==0:
										right = str(0)
									else:
										right = str(1)
									with codecs.open('zhidao_question_to_answer.txt','a+','utf-8') as f:
										# f.write(str(data)+'\r\n')
											if desc == '':
												s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+'\t'+title+'\t'+right+'\t'+str(like)).strip().replace('\n','').replace('\r','').strip('\n')
												f.write(s+'\r\n')
												f.close()
											else:
												s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+title+'\t'+right+'\t'+str(like)).strip().replace('\n','').replace('\r','').strip('\n')
												f.write(s+'\r\n')
												f.close()
							else:
								pass



		else:
			pass


test()
		
