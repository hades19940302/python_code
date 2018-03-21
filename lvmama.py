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
  'Cookie': 'uid=rBQOcVqqH0eQaxNhDuVPAg==; CoreID6=90534060778215210988125&ci=52710000|PC; _ga=GA1.2.256388324.1521098813; _gid=GA1.2.619805275.1521098813; _jzqckmp=1; fp_ver=4.5.1; BSFIT_EXPIRATION=1521946725471; BSFIT_OkLJUJ=FFFxSzdan22aXDUKsq4nXAUu8KZc7NJP; BSFIT_DEVICEID=PxXY63A4S4VIrQp43TwmbBh7VnaHBHTRMvJR6tFOGzKNOzbwbDWmG6aRjGDymFVW2Lbfv3tfxduPGLtwiviQJ3i34iJW6FroSb3qsUNK8vLxyLjUaXZe-XGVVuzmKwTyUAA_8j1A1cAbioCnNBTgQudO5e6R3CvM; lvsessionid=c68f7517-b55c-49dd-a0ef-45f993b3bd3a_15771908; cmTPSet=Y; _qzjc=1; Hm_lvt_cb09ebb4692b521604e77f4bf0a61013=1521098815,1521161055; _jzqc=1; PHPSESSID=mmurru36vmtu8bugjcfv79lic2; _jzqa=1.4118907848655464000.1521098818.1521161055.1521163702.3; JSESSIONID=B76BEE247C88D735E13C344376286BD3; _fmdata=sRlFka7c%2BM6%2FFz15LrSFK6kD7qLUnsi961JLkjda2YT7Y19Au2yQbdpRjIb7GjF%2F5WR54dLw5j%2FGB8YKuNANt1HYLumNwnugzIu5cLN9CB8%3D; _gat=1; _pzfxuvpc=1521098816629%7C7394215399127076966%7C6%7C1521163773120%7C3%7C1191948565222564347%7C1119836527223804368; _pzfxsvpc=1119836527223804368%7C1521163701449%7C2%7C; _qzja=1.1593916596.1521098821634.1521161054891.1521163701507.1521163701507.1521163773171.0.0.0.6.3; _qzjb=1.1521163701507.2.0.0.0; _qzjto=4.2.0; _jzqb=1.2.10.1521163702.1; 52710000|PC_clogin=l=1521163701&v=1&e=1521165574076; Hm_lpvt_cb09ebb4692b521604e77f4bf0a61013=1521163775',
  'Host': 'www.lvmama.com',
  'Origin': 'http://www.lvmama.com',
  'Proxy-Connection': 'keep-alive',
  'Referer': 'http://www.lvmama.com/lvyou/wenda/search/?q=%E6%97%A5%E6%9C%AC',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
  'X-Requested-With':'XMLHttpRequest',
}


def test():
    for i in range(2):
        url = 'http://www.lvmama.com/lvyou/ajax-wenda/get-more-search-list/' 
        payload = {'page':i,'keyword':'日本'}
        response = requests.post(url,data=payload, headers=headers, timeout=20, verify=False)

        json_data = json.loads(response.content)

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
                  'Cookie': 'uid=rBQOcVqqH0eQaxNhDuVPAg==; CoreID6=90534060778215210988125&ci=52710000|PC; _ga=GA1.2.256388324.1521098813; _gid=GA1.2.619805275.1521098813; _jzqckmp=1; fp_ver=4.5.1; BSFIT_EXPIRATION=1521946725471; BSFIT_OkLJUJ=FFFxSzdan22aXDUKsq4nXAUu8KZc7NJP; BSFIT_DEVICEID=PxXY63A4S4VIrQp43TwmbBh7VnaHBHTRMvJR6tFOGzKNOzbwbDWmG6aRjGDymFVW2Lbfv3tfxduPGLtwiviQJ3i34iJW6FroSb3qsUNK8vLxyLjUaXZe-XGVVuzmKwTyUAA_8j1A1cAbioCnNBTgQudO5e6R3CvM; lvsessionid=c68f7517-b55c-49dd-a0ef-45f993b3bd3a_15771908; cmTPSet=Y; _qzjc=1; Hm_lvt_cb09ebb4692b521604e77f4bf0a61013=1521098815,1521161055; _jzqc=1; PHPSESSID=mmurru36vmtu8bugjcfv79lic2; _jzqa=1.4118907848655464000.1521098818.1521161055.1521163702.3; _qzja=1.1593916596.1521098821634.1521161054891.1521163701507.1521163701507.1521163773171.0.0.0.6.3; _qzjto=4.2.0; Rvyz72RO3yiChuCn=ioFrJfW91W9Sh1BQ6ZagwFJaQfmyzRqXUuBw%2Bdwg45plUqC3XTucg0UlurfxEwxwiSOi3VFCBGddqZbyuTSPW%2Fx9edKGOaUdCwTds0zUF2M6cRL%2FjYdrlIxdMAPMMlJe2AnMfxn4weOJ4X4nrYEydMGgpRHVM5i7BBNcFENH%2FPtcx%2FlTdXmnjOfeP8bS6RmxtdA8wke1fL97LdUQsoDKlE1JzyXvPw2wDhmYFuj3FfZcelXi%2FSqgP1ZNloKdS92%2FvEB7aL3i1%2Fjwtuf4tPDfLsM04OYD%2B1mRdVVerEV7%2FIWkwxYR16CYtF%2Fi0kFzL1TLRHh5ObUnSgqeggWKzSWUn7Cb4kUb9hqoMh14IbI3pHEetk6ZvxNZ%2F6ZemiDE%2B1scvuANq1J27UhwolZOGZGF1OteL41QxwmIvjdQk72Nr3zYGgf16sB%2FVcuYXWTWyqSVu1CybR4QSGVBBKL6BVcr8w%3D%3D112fe4fe05e76594ed9761a3d5f43bdd3955882c; _fmdata=sRlFka7c%2BM6%2FFz15LrSFK6kD7qLUnsi961JLkjda2YT7Y19Au2yQbdpRjIb7GjF%2Fu3g7enJvRzNdHPFoXCHdKzILXSjge7Gl1TWYaHVfsJY%3D; JSESSIONID=E68DC5497B9B062CE384ED87D449CF51; _pzfxuvpc=1521098816629%7C7394215399127076966%7C9%7C1521167389071%7C5%7C4702607073969999067%7C4686101274959246527; _pzfxsvpc=4686101274959246527%7C1521167066608%7C2%7Chttp%3A%2F%2Fwww.lvmama.com%2Flvyou%2Fwenda%2Fsearch%2F%3Fq%3D%25E6%2597%25A5%25E6%259C%25AC; Hm_lpvt_cb09ebb4692b521604e77f4bf0a61013=1521167389; 52710000|PC_clogin=l=1521167063&v=1&e=1521169189685',
                  'Host': 'www.lvmama.com',
                  'Referer': 'http://www.lvmama.com/lvyou/wenda/search/?q=%E6%97%A5%E6%9C%AC',
                  'Upgrade-Insecure-Requests': '1',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
                }
                r = requests.get(url, headers=header, timeout=5)
                html = r.content.decode("utf-8")  # 解码
                html = re.sub(r'<br[ ]?/?>', '\n', html)
                selector = etree.HTML(html)
                title = selector.xpath('//div[@class="question-detail"]/p[@class="question-wrc-title"]/text()')[1]
                desc = selector.xpath('//div[@class="question-detail"]/p[@class="question-detail-section"]/text()')[0]
                answers = selector.xpath('//p[@class="answer-passage"]/text()')
                relations = selector.xpath('//div[@class="relation-modular common-box"]/ul/li/a/text()')
                for related_qt in relations :
                  with codecs.open('lvmama_question_question.txt','a+','utf-8') as f:
                    f.write('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+related_qt+'\r\n')
                    f.close()         

                if len(answers) == 0:
                    pass
                else:
                    for answer in answers:
                      print(answer)
                      with codecs.open('lvmama_question_answer.txt', 'a+', 'utf-8') as f:
                          f.write('1'+'\t'+'qid:'+id_+'\t'+title+'#'+desc+'\t'+answer+'\t'+'0'+'\t'+0+'\r\n')
                          f.close()

test()