#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/5/15 10:41
# @File    : download.py
# @copyright (c): Hades All Rights Reserved

import requests
from lxml import etree

def test():
    response = requests.get('http://10.20.0.106/nnit-openstack/')
    html = response.content
    selector = etree.HTML(html)
    urls = selector.xpath('//td/a/@href')
    f = open('urls.txt','a')
    for url in urls:
        print(url)
        f.write(url+'\n')
    f.close()

# test()

def write_in_to():
    f = open('urls.txt','rb')
    for line in f.readlines():
        print(line)
        response = requests.get('http://10.20.0.106/nnit-openstack/'+line.replace('\n','').replace('\r',''))
        with open(line.replace('\n','').replace('\r',''), "wb") as rpm:
            rpm.write(response.content)
write_in_to()