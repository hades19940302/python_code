#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/17 14:28
# @File    : cut.py
# @Software: PyCharm


f = open('qr_ids_not_in_ids_by_2018_04_20.txt','rb')
i = 1
for line in f.readlines()[55000:60000]:

    f = open('qr_ids_not_in_ids_by_2018_04_20_55000.txt','a')
    f.write(line.replace('\r',''))
    f.close()

