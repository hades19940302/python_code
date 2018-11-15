#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/2 11:25


# lines = []
# def test():
#     f = open('baiduzhidao_topics_list_2.txt','rb')
#     for line in f.readlines():
#         line = line.replace('\n','').replace('\r','').strip()
#         if line not in lines:
#             lines.append(line)
#             f= open('baiduzhidao_topics_list_3.txt','a')
#             f.write(line+'\n')
#             f.close()
#     f.close()


id1s = []
id2s = []
def test():
    f = open('baiduzhidao_ids_2.txt','rb')
    f1 = open('baiduzhidao_ids_3.txt','rb')
    for id1 in f.readlines():
        id1 = id1.replace('\r','').replace('\n','').strip()
        if id1 not in id1s:
            id1s.append(id1)

    for id2 in f1.readlines():
        id2 = id2.replace('\r','').replace('\n','').strip()
        if id2 not in id1s:
            f2 = open('baiduzhidao_ids_4.txt','a')
            print(id2)
            f2.write(id2+'\n')
            f2.close()



    f1.close()
    f.close()
test()