#!/usr/bin/env python
# coding=utf-8
# author=hades
# oshiete urls
from __future__ import print_function
from __future__ import division
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
import gzip
import StringIO
import time
import threadpool as tp
import urllib2
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

proxy_header = {
	'Host': 'ent.kuaidaili.com',
	'Connection': 'keep-alive',
	'Cache-Control': 'max-age=0',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	

	}

# proxys = ['182.86.189.174:61091',
# 	'121.237.138.249:21953',
# 	'58.253.147.9:61924',
# 	'117.21.111.26:32771',
# 	'223.245.213.159:40956',
# 	'27.31.101.152:46781',
# 	'183.143.72.243:63565',
# 	'117.26.41.230:13915',
# 	'123.163.150.172:60864',
# 	'120.33.247.128:64079',
# 	'123.162.127.97:43263',
# 	'49.73.240.171:47380',
# 	'27.10.162.67:48960',
# 	'117.68.194.238:33531',
# 	'121.237.136.54:21731',
# 	'180.118.135.254:64743',
# 	'121.205.73.4:44141',
# 	'42.54.76.31:27058',
# 	'183.159.83.215:16841',
# 	'121.235.194.67:30881',
# 	'61.143.45.12:41675',
# 	'113.57.97.222:45842',
# 	'122.246.48.132:24788',
# 	'113.128.27.135:34559',
# 	'125.105.49.75:30459',
# 	'115.223.127.197:41474',
# 	'60.169.114.137:39516',
# 	'114.232.163.25:61445',
# 	'222.212.169.239:26923',
# 	'61.176.66.50:15250',
# 	'49.85.3.72:56330',
# 	'183.143.8.124:18977',
# 	'125.119.44.60:52652',
# 	'60.168.173.122:21310',
# 	'60.172.124.45:40446',
# 	'117.69.179.93:65077',
# 	'49.64.212.220:57526',
# 	'119.127.17.6:36268',
# 	'113.117.105.166:11969',
# 	'123.52.76.140:19039',
# 	'183.32.220.138:44217',
# 	'115.223.76.109:19838',
# 	'36.248.132.137:55048',
# 	'59.63.53.128:65107',
# 	'111.74.75.41:43552',
# 	'49.76.205.129:10932',
# 	'119.116.78.92:36255',
# 	'223.246.121.54:13871',
# 	'183.52.105.166:51607',
# 	'115.213.251.231:44545',
# 	'121.206.19.171:16793',
# 	'153.0.49.47:25944',
# 	'180.115.65.11:15436',
# 	'221.225.98.107:48564',
# 	'123.163.128.59:21521',
# 	'221.232.234.210:21748',
# 	'115.221.118.105:60990',
# 	'60.167.23.224:17474',
# 	'117.69.200.46:27655',
# 	'113.121.243.129:59796',
# 	'182.240.253.204:17161',
# 	'182.126.15.223:12519',
# 	'123.169.5.51:46695',
# 	'113.121.241.189:52189',
# 	'183.149.48.36:18724',
# 	'117.95.200.64:49915',
# 	'120.40.253.140:49950',
# 	'221.232.193.78:65305',
# 	'175.152.102.123:41217',
# 	'140.250.153.180:38312',
# 	'222.94.149.214:38909',
# 	'117.28.163.100:52784',
# 	'59.62.166.26:46869',
# 	'117.68.195.27:54842',
# 	'222.245.181.217:32334',
# 	'218.91.94.205:64075',
# 	'49.64.24.54:24835',
# 	'121.206.20.250:60732',
# 	'49.85.1.164:28205',
# 	'113.57.35.211:48902',
# 	'119.96.192.173:27860',
# 	'125.112.197.104:30913',
# 	'60.182.188.249:22961',
# 	'117.43.0.3:18136',
# 	'59.32.37.32:50407',
# 	'113.122.38.182:37564',
# 	'180.121.135.203:44061',
# 	'121.237.138.22:17534',
# 	'183.52.104.148:32368',
# 	'60.175.196.30:23255',
# 	'36.33.25.80:34670',
# 	'42.55.180.139:20101',
# 	'113.121.242.88:24331',
# 	'59.57.46.146:33048',
# 	'222.245.186.203:59950',
# 	'1.196.158.169:65449',
# 	'60.17.233.246:61358',
# 	'175.146.94.156:60034',
# 	'125.112.202.207:43541',
# 	'180.122.144.230:54993',]
proxys = []
r_proxy=  requests.get('http://ent.kuaidaili.com/api/getproxy/?orderid=938176699822329&num=1000&quality=2&sort=1&format=json')
json_data = json.loads(r_proxy.content)
data = json_data['data']
proxy_list = data['proxy_list']

for proxy in proxy_list:
	if proxy not in proxys:
		proxys.append(proxy)

def get_multi_urls(file_name):
	lines = []
	f = open(file_name, 'r')
	for line in f.readlines():
		line = line.replace('\n','').replace('\r','').strip()
		if line not in lines:
			lines.append(line)

	return lines*5


def get_random_url(lines):
	url_numbers = len(lines)
	if url_numbers > 0:
		url_pos = random.randint(0, url_numbers-1)
	else:
		url_pos = 0

	return lines.pop(url_pos), lines

def test(xx):
	flag = 5
	urls = get_multi_urls('test.txt')
	while urls:
		url, urls = get_random_url(urls)
		id_ = url[33:-7]
		url = url.replace('\r','').replace('\n','').strip()+'?fr=iks&ie=utf-8'
		# url = 'https://zhidao.baidu.com/question/1702054658067875940.html?fr=iks&ie=utf-8'
		# f_has_read = open('has_read.txt','a')
		# f_has_read.write(url.replace('\r','')+'\n')
		# f_has_read.close()
		try:
			r_proxy = requests.get(
				'http://ent.kuaidaili.com/api/getproxy/?orderid=938176699822329&num=1000&quality=2&sort=1&format=json')
			json_data = json.loads(r_proxy.content)
			data = json_data['data']
			proxy_list = data['proxy_list']
		except:
			pass
		for proxy in proxy_list:
			if proxy not in proxys:
				proxys.append(proxy)
		while True:
			try:
				start = time.time()
				try:
					proxy = random.choice(proxys)
					response = requests.get(url,timeout=5,headers=headers,verify=False,proxies={"http":"http://"+proxy})
				except:
					continue
				html = response.content.decode('utf-8')
				requests.adapters.DEFAULT_RETRIES = 5
				if response.status_code != 200:
					proxys.remove(proxy)
					continue
				s = requests.session()
				s.keep_alive = False
				end = time.time()
				print(str(flag)+':' + 'succeed: ' + url + '\t' + " succeed in " + format(end - start, '0.4f') + 's!')
				flag = flag + 1
				sleep(random.randint(1,30))
				break
			except:
				print('switch proxy')
				continue

		html = re.sub(r'<br[ ]?/?>', '\n', html)
		selector = etree.HTML(html)
		question = selector.xpath('//div[@class="wgt-question-title"]/h2')
		if question == []:
			question = selector.xpath('//div[@class="mm-content-line w-question-box"]/div[@class="title"]/h2')
			if question == []:
				question = selector.xpath('//div[@class="wgt-question-title"]/h2')
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
						like = ['0']

			if like ==[]:
				pass
			else:
				if like[0] == '0' or like[0] == 0:
					pass
				else:
					if answers == []:
						print(url+'answers erro')
						answers = selector.xpath('//div[@class="full-content"]')
						with codecs.open('zhidao_question_to_answer_man_proxy.txt','a+','utf-8') as f:

							if desc == '':
								s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'\t'+answers[0].xpath('string(.)').strip().replace('\t','')+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
								f.write(s+'\r\n')
								f.close()
							else:
								s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'#'+desc.replace('\t','')+'\t'+answers[0].xpath('string(.)').strip().replace('\t','')+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
								f.write(s+'\r\n')
								f.close()

		else:
			answers = selector.xpath('//div[@class="full-content"]')
			like = selector.xpath('//div[starts-with(@class,"append")]/div/div[@class="question-meta-support question-meta-support-area"]/span/@data-support')
			if answers == [] or like == []:
				answers = selector.xpath('//div[@class="full-content"]')
				like = selector.xpath('//span[@class="js-question-meta-num question-meta-support-num"]/@data-support')

			with codecs.open('zhidao_question_to_answer_man_proxy.txt','a+','utf-8') as f:
					if desc == '':
						s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'\t'+answers[0].xpath('string(.)').strip().replace('\t','')+'\t'+'1'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
						f.write(s+'\r\n')
						f.close()
					else:
						s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'#'+desc.replace('\t','')+'\t'+answers[0].xpath('string(.)').strip().replace('\t','')+'\t'+'1'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
						f.write(s+'\r\n')
						f.close()


		for r_question_list_title in r_question_list_titles:

			with codecs.open('zhidao_question_to_question_man_proxy.txt','a+','utf-8') as f1:
				if desc == '':
					s = ('1'+'\t'+'qid:'+str(id_)+'\t'+question.xpath('string(.)').strip().replace('\t','')+'\t'+r_question_list_title.xpath('string(.)').strip().replace('\t','')).strip().replace('\n','').replace('\r','')
					f1.write(s+'\r\n')
					f1.close()
				else:
					s = ('1'+'\t'+'qid:'+str(id_)+'\t'+question.xpath('string(.)').strip().replace('\t','')+'#'+desc.replace('\t','')+'\t'+r_question_list_title.xpath('string(.)').strip().replace('\t','')).strip().replace('\n','').replace('\r','')
					f1.write(s+'\r\n')
					f1.close()
		answers2_list = []
		for i in range(5):
			r2_url = 'http://zhidao.baidu.com/mobile/replies?rn=6&new=1&hasLoadArgue=0&qid='+id_+'&samp_hit=246&pn='+str(i)+'&deleteArgue=0'
			headers2 = {
				'Host': 'zhidao.baidu.com',
				'X-Requested-With': 'XMLHttpRequest',
				'Accept-Language': 'zh-cn',
				'Accept-Encoding': 'br, gzip, deflate',
				'Accept': '*/*',
				'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D60 Safari/604.1',
			}
			while True:
				try:
					proxy = random.choice(proxys)
					r2 = requests.get(r2_url, headers=headers2,proxies={"http":"http://"+proxy} ,timeout=5, verify=False)
					html2 = r2.content.decode('utf-8')
					if r2.status_code != 200:
						proxys.remove(proxy)
						continue
					len_content = len(r2.content)
					requests.adapters.DEFAULT_RETRIES = 5
					s = requests.session()
					s.keep_alive = False
					sleep(random.randint(1,30))
					break
				except:
					continue
			if len_content == 13 or len_content == 47 or len_content == 404:
				break
			else:
				pass
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
												try:

													with codecs.open('zhidao_question_to_answer_man_proxy.txt','a+','utf-8') as f:
															if desc == '':
																s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'\t'+title[0].xpath('string(.)').strip().replace('\t','')+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
																f.write(s+'\r\n')
																f.close()
															else:
																s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'#'+desc.replace('\t','')+'\t'+title[0].xpath('string(.)').strip().replace('\t','')+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
																f.write(s+'\r\n')
																f.close()

												except:
													print('question erro:'+url)


							else:
								if title[0].xpath('string(.)').strip() not in answers2_list:
									answers2_list.append(title[0].xpath('string(.)').strip())

									if like== [] :
										pass
									else:
										if like[0] ==0 or like[0] =='0':
											pass
										else:

											with codecs.open('zhidao_question_to_answer_man_proxy.txt','a+','utf-8') as f:
													if desc == '':
														s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'\t'+title[0].xpath('string(.)').strip().replace('\t','')+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
														f.write(s+'\r\n')
														f.close()
													else:
														s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'#'+desc.replace('\t','')+'\t'+title[0].xpath('string(.)').strip().replace('\t','')+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
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

										with codecs.open('zhidao_question_to_answer_man_proxy.txt','a+','utf-8') as f:

												if desc == '':
													s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'\t'+title[0].xpath('string(.)').strip().replace('\t','')+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
													f.write(s+'\r\n')
													f.close()
												else:
													s = ('1'+'\t'+'qid:'+id_+'\t'+question.xpath('string(.)').strip().replace('\t','')+'#'+desc.replace('\t','')+'\t'+title[0].xpath('string(.)').strip().replace('\t','')+'\t'+'0'+'\t'+str(like[0])).strip().replace('\n','').replace('\r','').strip('\n')
													f.write(s+'\r\n')
													f.close()









args = ['xxxx']
pool = tp.ThreadPool(10)
reqs = tp.makeRequests(test, args)
[pool.putRequest(req) for req in reqs]
pool.wait()


