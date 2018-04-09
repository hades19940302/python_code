#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/9 10:04


def filter_by_difference():
    f = open('zhidao_question_to_answer_man_proxy.txt','r')
    for line in f.readlines():
        t =  line.find('qid:') #qid's position
        tt = line.find('\t',2) # \t's postion
        flag = line[-20:]
        f1 = open('zhidao_question_to_answer_man_proxy.txt', 'r')
        items = []
        lens = []
        for line1 in f1.readlines():
            if line1.find(flag)  != -1:
                items.append(line1)
                lens.append(len(line1))


        print(min(lens))
        f2 = open('zhidao_question_to_answer_man_proxy_filter.txt','a')
        f2.write(min(items))
        f2.close()


    f1.close()

    f.close()


filter_by_difference()