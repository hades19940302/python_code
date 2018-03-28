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
sys.setdefaultencoding("utf-8")
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# import pymysql
# from multiprocessing.dummy import Pool as ThreadPool
url_list = []
# url='https://cn.oshiete.goo.ne.jp/qa/list'
id_list = []
rb = {}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}  # 构造浏览器头信息

headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Content-Length': '33',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'uid=rBQOcVqqH0eQaxNhDuVPAg==; CoreID6=90534060778215210988125&ci=52710000|PC; _ga=GA1.2.256388324.1521098813; fp_ver=4.5.1; BSFIT_OkLJUJ=FFFxSzdan22aXDUKsq4nXAUu8KZc7NJP; _jzqa=1.4118907848655464000.1521098818.1521161055.1521163702.3; _qzja=1.1593916596.1521098821634.1521161054891.1521163701507.1521163701507.1521163773171.0.0.0.6.3; PHPSESSID=fv96vpeepk5jl30uctpovuig80; lvsessionid=a7da47bb-1513-4aa0-be6b-3e35329e4fc5_15084311; cmTPSet=Y; Hm_lvt_cb09ebb4692b521604e77f4bf0a61013=1521605413,1521608631,1521624524,1522110679; _gid=GA1.2.703979128.1522110680; BSFIT_EXPIRATION=1522932696390; BSFIT_DEVICEID=AjXOB77m76JsZ7F0KMYznkuQ5bOoPqmHnTpicEW6voAbL1rmkADjOu-HC9vAaYa-LrWYDjoFd2pdiuVYsBG76IZRe8tacs79-GYqVHfLlfvEwwek5LGpTECYMIGJlYLuNLbPI1EK1CICqIJW6hBaQctb_O9iUZ7i; Rvyz72RO3yiChuCn=5Br%2B%2BAgTPA1XegHwD7WVl8PsQJU9OEpHf%2F4dAsZ9zyE5CDqoqRE4K5VgZPynhgF3zfFv1WdFcs5vOpc1oA2gQn4f%2Ff1xJErnTFerxBwqAtFXeLZdRd3yqAOA4LpxKUXehbZMa9CYfy2rSRyj1Y8f1Y5CPhi7fJU735iUNtPBdgfGlh78SLpit8s41OMpC5IYFFg7mt%2BUY%2F727TAD%2FCMKkJxTa%2BhtsSBpNYj1V%2FpErgdWzsB4St5uM1iZVdj8OwIbWsVtWMd63PjeTJF0T5I10iZb5h8G77PpeMYPoizqlBLRso9Rlz%2B8hM%2FN5MfXnSB2DlU2hdRaF9DBpKyGDETwNZWOVvAe5L9j6mkccq5JpndK9%2FnG4HwpLRy%2BcUoaE3nAOBM%2FZ%2BjLuZQhmk1oBoKDMDvCoKG%2B%2BmkAzkFTYHGi5GKr67nbn1Lo9eL91TK7QSgS77iPBsu6XisZDEVpDr%2BRhA%3D%3D67a013e6822076d4eb2227b4a68b3626bee233da; _pzfxuvpc=1521098816629%7C7394215399127076966%7C26%7C1522111564097%7C10%7C1026014037312366489%7C6219815885919088546; _pzfxsvpc=6219815885919088546%7C1522110679125%7C7%7C; JSESSIONID=90BD0F0FD96B768B1FB9800811151120; _gat=1; Hm_lpvt_cb09ebb4692b521604e77f4bf0a61013=1522111564; 52710000|PC_clogin=l=1522110678&v=1&e=1522113364377; _fmdata=sRlFka7c%2BM6%2FFz15LrSFK6kD7qLUnsi961JLkjda2YT7Y19Au2yQbdpRjIb7GjF%2FVz4UpuMXFFNVQosOnvg2aXhdVysu2aBdG0IyyE28lGo%3D',
  'Host': 'www.lvmama.com',
  'Origin': 'http://www.lvmama.com',
  'Proxy-Connection': 'keep-alive',
  'Referer': 'http://www.lvmama.com/lvyou/wenda/search/?q=%E6%97%A5%E6%9C%AC',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
  'X-Requested-With':'XMLHttpRequest',
}


def test():
    for i in range(7):
        url = 'http://www.lvmama.com/lvyou/ajax-wenda/get-more-search-list/' 
        payload = {'page':i,'keyword':'日本'}
        response = requests.post(url,data=payload, headers=headers, timeout=20, verify=False)
        json_data = json.loads(response.content)
        if json_data['islast']:
          print(i)
          pass
        else:
          data = json_data['data']
          html = data.decode('utf-8')
          html = re.sub(r'<br[ ]?/?>','\n',html)
          selector = etree.HTML(html)
          links = selector.xpath('//p[@class="question-wrc-title"]/a/@href')
          for link in links:
              # url = 'http://www.lvmama.com/lvyou/wenda/da-6762.html'
              id_ = link[5:-5]
              url = 'http://www.lvmama.com/lvyou/wenda' + link[1:]
              if url not in url_list:
                  url_list.append(url)
                  header = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Cookie': 'uid=rBQOcVqqH0eQaxNhDuVPAg==; CoreID6=90534060778215210988125&ci=52710000|PC; _ga=GA1.2.256388324.1521098813; fp_ver=4.5.1; BSFIT_EXPIRATION=1521946725471; BSFIT_OkLJUJ=FFFxSzdan22aXDUKsq4nXAUu8KZc7NJP; BSFIT_DEVICEID=PxXY63A4S4VIrQp43TwmbBh7VnaHBHTRMvJR6tFOGzKNOzbwbDWmG6aRjGDymFVW2Lbfv3tfxduPGLtwiviQJ3i34iJW6FroSb3qsUNK8vLxyLjUaXZe-XGVVuzmKwTyUAA_8j1A1cAbioCnNBTgQudO5e6R3CvM; _jzqa=1.4118907848655464000.1521098818.1521161055.1521163702.3; _qzja=1.1593916596.1521098821634.1521161054891.1521163701507.1521163701507.1521163773171.0.0.0.6.3; _fmdata=sRlFka7c%2BM6%2FFz15LrSFK6kD7qLUnsi961JLkjda2YT7Y19Au2yQbdpRjIb7GjF%2FZ%2BbpGXlbnhuFXAswAYE4WN0Z%2BIwHx95xTHJPLa9C1i8%3D; PHPSESSID=fv96vpeepk5jl30uctpovuig80; lvsessionid=a7da47bb-1513-4aa0-be6b-3e35329e4fc5_15084311; cmTPSet=Y; JSESSIONID=1EB89B3CD60E8C8A438CC4E54D878BA2; _pzfxuvpc=1521098816629%7C7394215399127076966%7C20%7C1522110679131%7C10%7C1026014037312366489%7C6219815885919088546; _pzfxsvpc=6219815885919088546%7C1522110679125%7C1%7C; Hm_lvt_cb09ebb4692b521604e77f4bf0a61013=1521605413,1521608631,1521624524,1522110679; Hm_lpvt_cb09ebb4692b521604e77f4bf0a61013=1522110679; _gid=GA1.2.703979128.1522110680; _gat=1; 52710000|PC_clogin=l=1522110678&v=1&e=1522112480222',
                    'Host': 'www.lvmama.com',
                    'Referer': 'http://www.lvmama.com/lvyou/wenda/search/?q=%E6%97%A5%E6%9C%AC',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
                  }
                  r = requests.get(url, headers=header, timeout=5)
                  html = r.content.decode("utf-8")  # 解码
                  html = re.sub(r'<br[ ]?/?>', '\n', html)
                  selector = etree.HTML(html)
                  title = selector.xpath('//div[@class="question-detail"]/p[@class="question-wrc-title"]/text()')[1].strip()
                  desc = selector.xpath('//p[@class="question-detail-section"]/text()')
                  if desc == []:
                    desc = ''
                  else:
                    desc = desc[0]
                  answers = selector.xpath('//p[@class="answer-passage"]/text()')
                  relations = selector.xpath('//div[@class="relation-modular common-box"]')[0].xpath('./ul/li/a/text()')
                  for related_qt in relations :
                    with codecs.open('lvmama_question_question.txt','a+','utf-8') as f1:
                      if desc == '':
                          s = ('1'+'\t'+'qid:'+id_+'\t'+title+'\t'+related_qt).strip().replace('\n','').replace('\r','')
                          f1.write(s+'\r\n')
                          f1.close()
                      else:
                          s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+related_qt).strip().replace('\n','').replace('\r','')
                          f1.write(s+'\r\n')
                          f1.close()      

                  # if len(answers) == 0:
                  #     pass
                  # else:
                  #     for answer in answers:
                  #       with codecs.open('lvmama_question_answer.txt', 'a+', 'utf-8') as f:
                  #         if desc == '':
                  #             s = ('1'+'\t'+'qid:'+id_+'\t'+title+'\t'+answer+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
                  #             f.write(s+'\r\n')
                  #             f.close()
                  #         else:
                  #             s = ('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+answer+'\t'+'0'+'\t'+'0').strip().replace('\n','').replace('\r','')
                  #             f.write(s+'\r\n')
                  #             f.close()




test()