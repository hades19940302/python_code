#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:hades 
@file: test.py 
@time: 2018/07/{DAY} 
"""

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1530853445,1530858397,1531104172,1531107760; _m7e_session=830514eef5ef3caaac73b0a137510bc4; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fp%2F8936b84d909a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221622dac4b66508-005c5afdf13d7a-3a61430c-1327104-1622dac4b67331%22%2C%22%24device_id%22%3A%221622dac4b66508-005c5afdf13d7a-3a61430c-1327104-1622dac4b67331%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1531107883',
    'Host': 'www.jianshu.com',
    'If-None-Match': 'W/"6368acf6c803fd0d1cb7d2dab4d20741"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
import requests
def test():
    while True:
        response = requests.get('https://www.jianshu.com/p/8936b84d909a',headers=headers)
        print(response.content)
test()