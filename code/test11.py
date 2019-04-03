#!/usr/bin/env python
# coding=utf-8
# author=hades
# oshiete urls

import requests 


headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Cookie': 'tp_sid=7fed5ab240a624d7; Hm_lvt_d7f4104c23e10d73303b198308c9b82d=1521098959,1521598007,1521612944,1521775183; tp_lastrefresh=1; Hm_lpvt_d7f4104c23e10d73303b198308c9b82d=1521777085',
	'Host': 'www.zhcpic.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		}

def test():
	r = requests.get('https://www.zhcpic.com/gonglue/ask-269862.html',headers=headers,verify=False)
	print(r.content)

test()