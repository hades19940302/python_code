#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/17 11:18
# @File    : analysis.py
# @Software: PyCharm

# 完成对相关url的分析：去重，爬取有待完善

ids = []
def filter():
    # 取到相关问题的qid等待准备比较
    f = open('qr_urls_4.txt','rb')
    for line in f.readlines():
        start = line.index('question/')
        end = line.index('.html?')
        # print(line[28:end])
        id_ = line[28:end]
        if id_ not in ids:
            ids.append(id_)
            f = open('qr_ids_2.txt','a')
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


# analysis()

def duplicate_removal():
    f = open('ids.txt','rb')
    for line in f.readlines():
        id_ = line.replace('\r','')
        if id_ not in ids:
            ids.append(id_)
            f = open('by_2018_04_19_ids.txt','a')
            f.write(id_)
            f.close()

    f.close()

# duplicate_removal()


def confirm_in_ids():
    f = open('ids.txt','rb')
    qa_ids = []
    for line in f.readlines():
        id_qa = line.replace('\n','').replace('\r','').strip()
        if id_qa not in qa_ids:
            qa_ids.append(id_qa)
            f = open('not_repeat_ids.txt','a')
            f.write(id_qa+'\n')
            f.close()

    f.close()
    f1 = open('qr_ids_2.txt','rb')
    qq_ids = []
    for line in f1.readlines():
        id_qq = line.replace('\n','').replace('\r','').strip()
        if id_qq not in  qq_ids:
            qq_ids.append(id_qq)
            if id_qq not in qa_ids:
                f = open('qr_ids_2_not_in_ids.txt','a')
                f.write(id_qq+'\n')
                f.close()

    f1.close()

# confirm_in_ids()
qr_ids = []
def confirm_qr2_not_in_qr1():
    fa = open('qr_ids.txt','rb')
    for line in fa.readlines():
        id_ = line.replace('\n','').replace('\r','').strip()
        if id_ not in qr_ids:
            qr_ids.append(id_)
            f = open('qr_ids_not_repeat.txt','a')
            f.write(id_+'\n')
            f.close()

    fa.close()
    f1 = open('qr_ids_2_not_in_ids.txt','rb')
    qq_ids = []
    for line in f1.readlines():
        id_qq = line.replace('\n','').replace('\r','').strip()
        if id_qq not in  qq_ids:
            qq_ids.append(id_qq)
            if id_qq not in qr_ids:
                f = open('qr_ids_2_not_in_qr_ids.txt','a')
                f.write(id_qq+'\n')
                f.close()


# confirm_qr2_not_in_qr1()

def confirm_not_in_qr_not_ids():
    f_qa = open('ids.txt','rb')
    for line in f_qa.readlines():
        id_qa = line.replace('\r','').replace('\n','').strip()
        if id_qa not in ids:
            ids.append(id_qa)
            f = open('ids_by_2018_04_20_1.txt','a')
            f.write(id_qa+'\n')
            f.close()

    f_qa.close()

    f_qq = open('qr_ids.txt','rb')
    for line in f_qq.readlines():
        id_qq = line.replace('\r','').replace('\n','').strip()
        if id_qq not in qr_ids:
            qr_ids.append(id_qq)
            f =open('qr_ids_by_2018_04_20_1.txt','a')
            f.write(id_qq+'\n')
            f.close()
            if id_qq not in ids:
                f = open('qr_ids_not_in_ids_by_2018_04_20_1.txt','a')
                f.write(id_qq+'\n')
                f.close()

    f_qq.close()


confirm_not_in_qr_not_ids()