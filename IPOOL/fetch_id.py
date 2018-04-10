#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/10 9:52


ids = []
def fetch_ids():
    f = open('baiduzhidao_url_list_sh.txt','r')
    for line in f.readlines():
        id_ = line[34:-5]
        if id_ not in ids:
            ids.append(id_)
            f = open('zhidao_ids_sh.txt','a')
            f.write(id_+'\n')
            f.close()


fetch_ids()



