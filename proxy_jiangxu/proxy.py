#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/8 11:30

"""使用urllib2请求代理服务器
请求http和https网页均适用
"""

import urllib2
import base64
import zlib
import random
import requests

#要访问的目标网页
page_url = "http://icanhazip.com/"

#代理服务器
proxy = "59.38.241.25:23916"

proxys  = [
	'218.14.55.246:57112',
	'222.185.223.40:57112',
	'218.14.140.183:57112',
	'1.193.237.77:57112',
	'117.43.0.232:57112',
	'218.73.135.134:57112',
	'27.8.160.228:57112',
	'27.11.137.108:57112',
	'183.150.160.11:57112',
	'140.250.135.186:57112',
	'123.53.118.70:57112',
	'59.32.37.125:57112',
	'218.14.49.194:57112',
	'115.213.200.227:57112',
	'119.142.77.95:57112',
]

proxy = random.choice(proxys)
#用户名和密码(私密代理/独享代理)
username = "rongshu"
password = "rongshu0411"

print(proxy)
def test():
    req = urllib2.Request(page_url)
    req.add_header("Accept-Encoding", "Gzip") #使用gzip压缩传输数据让访问更快
    req.add_header("Proxy-Authorization", "Basic %s" % base64.b64encode(b'%s:%s' % (username, password)))
    req.set_proxy(proxy, "http")
    r = urllib2.urlopen(req)

    print r.code
    content_encoding = r.headers.getheader("Content-Encoding")
    if content_encoding and "gzip" in content_encoding:
        print zlib.decompress(r.read(), 16+zlib.MAX_WBITS) #获取页面内容
    else:
        print r.read()

def test2():
    page_url = "http://dev.kuaidaili.com/testproxy"

    # 代理服务器

    # 用户名和密码(私密代理/独享代理)

    proxies = {'http': 'http://%s' % proxy, }
    headers = {
        "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
        "Proxy-Authorization": "Basic %s" % base64.b64encode(b'%s:%s' % (username, password)),
    # 不需要验证(如开放代理)，就不带这个header
    }

    r = requests.get(page_url, proxies=proxies, headers=headers)

    print r.status_code  # 获取Reponse的返回码

    if r.status_code == 200:
        r.enconding = "utf-8"  # 设置返回内容的编码
        print r.content  # 获取页面内容


test2()