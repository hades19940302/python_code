#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/18 17:07
# @File    : filter.py
# @Software: PyCharm

ids = []
f = open('qa.txt','rb')
for line in f.readlines():
    tt_qa = line.index('\t', 2)
    id_qa = line[6:tt_qa]
    f = open('qq.txt','rb')
    for line in f.readlines():
        tt_qq = line.index('\t', 2)
        id_qq = line[6:tt_qq]
        if id_qa == id_qq:
            f = open('qq_finally.txt','a')
            f.write(line.replace('\r',''))
            f.close()

f.close()


