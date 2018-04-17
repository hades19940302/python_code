#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/17 11:18
# @File    : analysis.py
# @Software: PyCharm

# 完成对相关url的分析：去重，爬取有待完善

ids = []
def filter():
    # 取到相关问题的qid来准备比较
    f = open('qr_urls_2018_04_17_10_11.txt','rb')
    for line in f.readlines():
        start = line.index('question/')
        end = line.index('.html?')
        # print(line[28:end])
        id_ = line[28:end]
        if id_ not in ids:
            ids.append(id_)
            f = open('qr_ids.txt','a')
            f.write(id_+'\n')
            f.close()

    f.close()


# filter()

def analysis():
    ids = []
    f = open('ids.txt','rb')
    for line in f.readlines():
        line = line.replace('\n','').replace('\r','').strip()
        if line not in ids:
            ids.append(line)

    f1 = open('qr_ids.txt','rb')
    for line in f1.readlines():
        line = line.replace('\n','').replace('\r','').strip()
        if line not in ids:
            f = open('qr_ids_not_in.txt','a')
            f.write(line+'\n')
            f.close()

    f.close()


analysis()
