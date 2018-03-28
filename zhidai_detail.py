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
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	# 'Cookie': 'IKUT=4099; BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; locale=zh; H_PS_PSSID=1446_21101_22158; PSINO=2; pgv_pvi=4774521856; pgv_si=s6383790080; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1522048693,1522118202,1522121671,1522129987; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1522135292; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1522043824,1522047460,1522048637,1522135295; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1522135295',
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
	f1 = open('baiduzhidao_url_list_3.txt','rb')
	i = 1
	for url in f1.readlines():
		id_ = url[34:-7]
		if id_ not in id_list:
			id_list.append(id_)
			while True:
				try:
					r = requests.get(url,headers=headers,timeout=20,verify=False)
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					sleep(10)
					break


				except:
					print('let us go  sleep!!!')
					sleep(20)
					print('ogo')
					continue	
			try:
				html = r.content.decode("utf-8")  # 解码
				html = re.sub(r'<br[ ]?/?>', '\n', html)
				selector = etree.HTML(html)
				question = selector.xpath('//div[@class="wgt-question-title"]/h2')
				if question == []:
					question = selector.xpath('//div[@class="mm-content-line w-question-box"]/div[@class="title"]/h2')
					if question == []:
						pass
					else:
						question=question[0]
				else:
					question = question[0]
				question_desc = selector.xpath('//div[@class="wgt-question-desc-inner"]')
				bingo = selector.xpath('//div[@class="best-answer-icon"]')
				r_question_list_titles  = selector.xpath('//div[@class="w-question-list"]/a/span[@class="r-question-list-title "]')

				if question_desc == []:
					desc = selector.xpath('//div[@class="wgt-question-desc-inner"]')
					if desc == []:
						print(url+'desc 空')
						desc = ''
					else:
						desc = selector.xpath('//div[@class="wgt-question-desc-inner"]')[0].xpath('string(.)').strip()
				else:
					desc = question_desc[0].xpath('string(.)').strip()

				if bingo == []:
					answers = selector.xpath('//div[@class="w-reply-container w-reply-item-normal"]/div[@class="w-detail-full"]/div[@class="w-detail-container w-detail-0"]/div/div')
					like = selector.xpath('//div[@class="w-reply-container w-reply-item-normal"]/div[@class="append"]/div/div[@class="question-meta-support question-meta-support-area"]/span/@data-support')
					if like == []:
						like = selector.xpath('//div[starts-with(@class,"w-support ico-tmb enhance-sup")]/b/text()')
						if like == []:
							like = selector.xpath('//span[@class="js-question-meta-num question-meta-support-num"]/@data-support')
							if like == []:
								print(url+'like erro')

					if like ==[]:
						pass
					else:
						if like[0] == '0' or like[0] == 0:
							pass
						else:
							if answers == []:
								print(url+'answers erro')
								answers = selector.xpath('//div[@class="full-content"]')
								with codecs.open('zhidao_question_to_answer_man.txt','a+','utf-8') as f:

									if desc == '':
										s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'\t'+answers[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
										f.write(s+'\r\n')
										f.close()
									else:
										s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+answers[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
										f.write(s+'\r\n')
										f.close()

				else:
					answers = selector.xpath('//div[@class="full-content"]')
					like = selector.xpath('//div[starts-with(@class,"append")]/div/div[@class="question-meta-support question-meta-support-area"]/span/@data-support')
					if answers == [] or like == []:
						print(url+'bingo answer erro')

					with codecs.open('zhidao_question_to_answer_man.txt','a+','utf-8') as f:
							if desc == '':
								s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'\t'+answers[0].xpath('string(.)').strip()+'\t'+'1'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
								f.write(s+'\r\n')
								f.close()
							else:
								s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+answers[0].xpath('string(.)').strip()+'\t'+'1'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
								f.write(s+'\r\n')
								f.close()


				for r_question_list_title in r_question_list_titles:

					with codecs.open('zhidao_question_to_question_man.txt','a+','utf-8') as f1:
						if desc == '':
							s = ('1'+'\t'+'qid:'+str(id_)+'\t'+question.xpath('string(.)').strip()+'\t'+r_question_list_title.xpath('string(.)').strip()).strip().replace('\n','').replace('\r','')
							f1.write(s+'\r\n')
							f1.close()
						else:
							s = ('1'+'\t'+'qid:'+str(id_)+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+r_question_list_title.xpath('string(.)').strip()).strip().replace('\n','').replace('\r','')
							f1.write(s+'\r\n')
							f1.close()
				answers2_list = []
				for i in range(5):
					r2_url = 'https://zhidao.baidu.com/mobile/replies?rn=6&new=1&hasLoadArgue=0&qid='+id_+'&samp_hit=246&pn='+str(i)+'&deleteArgue=0'
					headers2 = {
						'Host': 'zhidao.baidu.com',
						'X-Requested-With': 'XMLHttpRequest',
						'Accept-Language': 'zh-cn',
						'Accept-Encoding': 'br, gzip, deflate',
						# 'Cookie': 'IKUT=4099; BAIDUID=D36E55B433347B48F9BFE6BD1CB48B62:FG=1; BIDUPSID=D36E55B433347B48F9BFE6BD1CB48B62; PSTM=1521028828; locale=zh; H_PS_PSSID=1446_21101_22158; PSINO=2; pgv_pvi=4774521856; pgv_si=s6383790080; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1522048693,1522118202,1522121671,1522129987; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1522135292; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1522043824,1522047460,1522048637,1522135295; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1522135295',
						'Accept': '*/*',
						'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D60 Safari/604.1',
					}
					while True:
						try:
							r2 = requests.get(r2_url,headers=headers2,timeout=50,verify=False)
							requests.adapters.DEFAULT_RETRIES = 5
							s = requests.session()
							s.keep_alive = False
							sleep(10)
							break
						except:
							print('let us go  sleep!!!')
							sleep(20)
							print('ogo')
							continue
					try:
						html2 = r2.content.decode("utf-8")  # 解码
						html2 = re.sub(r'<br[ ]?/?>', '\n', html2)
						selector2 = etree.HTML(html2)
						if selector2 == '' or selector2 == None:
							pass
						else:
							answers2 = selector2.xpath('//div[starts-with(@class,"w-reply-container")]')
							if answers2 == [] :
								pass
							else:
								for answer2 in answers2:
									like = answer2.xpath('./div[@class="append"]/div/div[@class="question-meta-support question-meta-support-area"]/span/@data-support')
									title = answer2.xpath('./div/div[@class="w-detail-full"]/div[@class="w-detail-container w-detail-"]/div/div')
									if title == []:
										title = answer2.xpath('./div/div[@class="w-detail-full"]/div/div/div')
										if title == []:
											title = answer2.xpath('./div/div/div/div')
											if title == []:
												print(r2_url)
											else:
												if title[0].xpath('string(.)').strip() not in answers2_list:
													answers2_list.append(title[0].xpath('string(.)').strip())
													if like== [] :
														pass
													else:
														if like[0] ==0 or like[0] =='0':
															pass
														else:

															with codecs.open('zhidao_question_to_answer_man.txt','a+','utf-8') as f:
																	if desc == '':
																		s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'\t'+title[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
																		f.write(s+'\r\n')
																		f.close()
																	else:
																		s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+title[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
																		f.write(s+'\r\n')
																		f.close()										


										else:
											if title[0].xpath('string(.)').strip() not in answers2_list:
												answers2_list.append(title[0].xpath('string(.)').strip())

												if like== [] :
													pass
												else:
													if like[0] ==0 or like[0] =='0':
														pass
													else:

														with codecs.open('zhidao_question_to_answer_man.txt','a+','utf-8') as f:
																if desc == '':
																	s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'\t'+title[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
																	f.write(s+'\r\n')
																	f.close()
																else:
																	s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+title[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
																	f.write(s+'\r\n')
																	f.close()

									else:
										if title[0].xpath('string(.)').strip() not in answers2_list:

											answers2_list.append(title[0].xpath('string(.)').strip())
											if like== [] :
												pass
											else:
												if like[0] ==0 or like[0] =='0':
													pass
												else:

													with codecs.open('zhidao_question_to_answer_man.txt','a+','utf-8') as f:

															if desc == '':
																s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'\t'+title[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
																f.write(s+'\r\n')
																f.close()
															else:
																s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip()+'#'+desc+'\t'+title[0].xpath('string(.)').strip()+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
																f.write(s+'\r\n')
																f.close()


					except:
						print('utf-8 erro'+r2_url)
			except:
				print('utf-8 erro '+url)





test()	
# args = ['xxxx','aaa','a']
# pool = tp.ThreadPool(20)
# reqs = tp.makeRequests(test, args)
# [pool.putRequest(req) for req in reqs]
# pool.wait()
		
