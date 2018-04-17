#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/16 11:04
# @File    : dowload.py
# @Software: PyCharm


titles = []
rq_titles = []
ids = []
def get_rq_urls(file_name):
    # 获取已知有效数据的qid
    for name in file_name:
        f = open(name,'rb')
        try:
            for line in f.readlines():
                tt = line.index('\t',2)
                id_ = line[6:tt]
                if id_ not in ids:
                    ids.append(id_)
                    f = open('ids.txt','a')
                    f.write(id_+'\n')
                    f.close()
                    print(id_)

        except:
            pass

file_name = ['qq_1_24949.txt','qq_2_14307.txt','qq_3_26505.txt']


def mosaic_urls():
    # 根据不在原本qid集合里的id重新组织URL
    f = open('qr_ids_not_in.txt','rb')
    for line in f.readlines():
        url = 'https://zhidao.baidu.com/question/'+line.replace('\n','').replace('\r','')+'.html'
        f = open('qr_urls_not_in.txt','a')
        f.write(url+'\n')
        f.close()

    f.close()

mosaic_urls()
# get_rq_urls(file_name)