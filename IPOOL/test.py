#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""使用urllib2请求代理服务器
请求http和https网页均适用
"""

import urllib2
import base64
import zlib
import time
import random
import requests
import json
import StringIO
import gzip

proxys = []
def test():
    flag = 20
    print(flag/20)


    if (flag / 20) == 1:
        r_proxy = requests.get(
            'http://ent.kuaidaili.com/api/getproxy/?orderid=938176699822329&num=1000&quality=2&sort=1&format=json')
        json_data = json.loads(r_proxy.content)
        data = json_data['data']
        proxy_list = data['proxy_list']

        for proxy in proxy_list:
            if proxy not in proxys:
                proxys.append(proxy)
    while True:
        url = 'http://zhidao.baidu.com'
        # try:
        flag = flag + 1
        start = time.time()
        proxy = random.choice(proxys)
        req = urllib2.Request(url)
        # req.add_header("Accept",
        #                "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
        # req.add_header("Accept-Language", "zh-CN,zh;q=0.9")
        # req.add_header("Accept-Encoding", "gzip, deflate")  # 使用gzip压缩传输数据让访问更快
        # req.add_header("User-Agent",
        #                "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25")
        # req.set_proxy(proxy, "http")
        # r = urllib2.urlopen(req)
        # r = r.read()
        # data = StringIO.StringIO(r)
        # gzipper = gzip.GzipFile(fileobj=data)
        response = requests.get(url,proxies={"http":"http://"+proxy})
        requests.adapters.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        # html = gzipper.read()
        print(response.content)
        end = time.time()
        print('succeed: ' + url + '\t' + " succeed in " + format(end - start, '0.4f') + 's!')
        break
        # except:
        #     continue


test()

