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
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list=[]
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
rb = {}
pro = ['112.95.56.203:8118',
		'222.76.187.42:8118',
		'221.224.49.237:3128',
		'113.105.201.31:3128',
		'1.196.55.187:61202',
		'27.215.245.246:61234',
		'61.135.217.7:80',
		'122.114.31.177:808',
		'180.113.45.132:8118',
		'183.143.53.87:61234',
		'116.55.77.81:61202',
		'27.19.77.33:61202',
		'183.23.75.66:61234',
		'59.48.148.226:61202',
		'221.224.49.237:3128']
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}  # 构造浏览器头信息

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
	for i in range(1):
		url = 'https://zhidao.baidu.com/msearch/ajax/getsearchlist?word=%E6%97%A5%E6%9C%AC%E6%97%85%E6%B8%B8&pn='+str(i)
		response = requests.get(url,headers=headers,timeout=50,verify=False)
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		s.keep_alive = False
		json_data = json.loads(response.content)
		data = json_data['data']
		entry = data['entry']
		for en in entry:
			# url = 'https://zhidao.baidu.com/question/1732180052597957147.html'
			en = json.dumps(en)
			en = json.loads(en)
			# url = 'https://zhidao.baidu.com'+en['url']
			url = 'https://zhidao.baidu.com/question/587241032.html'
			if url not in url_list:
				url_list.append(url)
				r = requests.get(url,headers=headers,timeout=50)
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				# id_ = en['url'][10:-5]
				id_ = '587241032'
		        
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

					with codecs.open('zhidao_question_to_question_1.txt','a+','utf-8') as f1:
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


				answers = selector.xpath('//div[@class="w-detail-full"]')
				bingo = selector.xpath('//div[@class="best-answer-icon"]')
				if len(answers)==0:
					pass
				else:
					for answer1 in answers:
						tmp = answer1.xpath('../div[@class="append"]/div/div')[3].xpath('./span/text()')
						title = answer1.xpath('./div/div/div/text()')[0]
						print(tmp)
						if tmp == [] or tmp[0]==0:
							pass
						else:
							like = tmp[0]
							if len(bingo)==0:
								right = str(0)
							else:
								right = str(1)
								print(title)
							with codecs.open('zhidao_question_to_answer_1.txt','a+','utf-8') as f:
									if desc == '':
										s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+'\t'+title+'\t'+right+'\t'+str(like)).strip().replace('\n','').replace('\r','')
										f.write(s+'\r\n')
										f.close()
									else:
										s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+title+'\t'+right+'\t'+str(like)).strip().replace('\n','').replace('\r','')
										f.write(s+'\r\n')
										f.close()



				r2_url = 'https://zhidao.baidu.com/mobile/replies?rn=6&new=1&hasLoadArgue=0&qid='+id_+'&samp_hit=246&pn=0&deleteArgue=0'
				headers2 = {
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'zh-CN,zh;q=0.9',
					'Cache-Control': 'max-age=0',
					'Connection': 'keep-alive',
					'Cookie': 'BAIDUID=8BFD7A79D7DA63A6065E3D74030C36A5:FG=1; BIDUPSID=8BFD7A79D7DA63A6065E3D74030C36A5; PSTM=1520907823; H_PS_PSSID=1442_21109_18560_17001_20718; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1521436652,1521448861,1521452532,1521506139; H_WISE_SIDS=110317_122743_114743_122651_120192_118894_118874_118849_118818_118792_120549_107318_121937_117330_121861_122788_122736_122138_122672_120851_120035_116407_122668_122623_122663_110085_122026_122302; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1521512230; PSINO=2; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1521512688,1521515539,1521515549,1521516329; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1521516506',
					'Host': 'zhidao.baidu.com',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
				}
				r2 = requests.get(r2_url,headers=headers2,timeout=50)
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				s.keep_alive = False
				html2 = r2.content.decode("utf-8")  # 解码
				html2 = re.sub(r'<br[ ]?/?>', '\n', html2)
				selector2 = etree.HTML(html2)	
				answers2 = selector2.xpath('//div[@class="w-detail-full"]')
				bingo2 = selector2.xpath('//div[@class="best-answer-icon"]')
				print(answers2)

				if answers2 == [] :
					pass
				else:
					for answer2 in answers2:
						tmp = answer2.xpath('./following-sibling::div[1]/div/div[@class="question-meta-support question-meta-support-area"]/span/@data-support')
						title = answer2.xpath('./div')[0].xpath('./div/div/text()')[0]
						if tmp==[] or title == [] or tmp[0] == 0 or tmp[0] == '0' :
							pass
						else:
							like = tmp[0]
							if len(bingo2)==0:
								right = str(0)
							else:
								right = str(1)
							with codecs.open('zhidao_question_to_answer_1.txt','a+','utf-8') as f:
								# f.write(str(data)+'\r\n')
									if desc == '':
										s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+'\t'+title+'\t'+right+'\t'+str(like)).strip().replace('\n','').replace('\r','').strip('\n')
										f.write(s+'\r\n')
										f.close()
									else:
										s = ('1'+'\t'+'qid:'+id_+'\t'+question+'#'+desc+'\t'+title+'\t'+right+'\t'+str(like)).strip().replace('\n','').replace('\r','').strip('\n')
										f.write(s+'\r\n')
										f.close()

	



test()