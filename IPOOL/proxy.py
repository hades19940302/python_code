#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/9 16:19

"""使用urllib2请求代理服务器
请求http和https网页均适用
"""

import urllib2
import base64
import zlib

#
# #要访问的目标网页
# page_url = "https://zhidao.baidu.com"
#
# #代理服务器
# proxy = "114.236.1.85:18478"
#
# #用户名和密码(私密代理/独享代理)
# username = "372941497"
# password = "y269nzcz"
#
# req = urllib2.Request(page_url)
# req.add_header("Accept-Encoding", "Gzip") #使用gzip压缩传输数据让访问更快
# req.add_header("Proxy-Authorization", "Basic %s" % base64.b64encode(b'%s:%s' % (username, password)))
# req.set_proxy(proxy, "https")
# r = urllib2.urlopen(req)
#
# print r.code
# content_encoding = r.headers.getheader("Content-Encoding")
# if content_encoding and "gzip" in content_encoding:
#     print zlib.decompress(r.read(), 16+zlib.MAX_WBITS) #获取页面内容
# else:
#     print r.read() #获取页面内容
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)

import requests

def test_proxy():
    s = requests.Session()
    s.mount('https://', MyAdapter())
    f = s.get('https://zhidao.baidu.com',proxies={"https":"http://114.215.95.188:3128"})
    print(f.content)

test_proxy()