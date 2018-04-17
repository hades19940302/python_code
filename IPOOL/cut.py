#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/17 14:28
# @File    : cut.py
# @Software: PyCharm


f = open('qr_urls_not_in.txt','rb')
i = 1
for line in f.readlines()[40000:50000]:
    f = open('qr_urls_not_in_5','a')
    f.write(line.replace('\r',''))
    f.close()


    pass
