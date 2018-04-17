#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/3/14 9:49
# @File    : answer_spider.py
# @Software: PyCharm

import scrapy
import json
import datetime
import time
from zhidao.items import TopicItem
# 爬取题目


class ZhidaoSpider(scrapy.Spider):

    def __init__(self):
        self.flag = 1
    name = 'answer'
    allowd_domains = ["https://m.baidu.com/"]
    start_urls = ['https://m.baidu.com/his?callback=json&type=3&pic=1&net=1&hisdata=[{"kw":"日本旅游","time":1520988178}]&_=1520988906089']



    url_list = []
    topics_list = []
    def parse(self, response):
        item = TopicItem()
        all_data = json.loads(response.body)
        with open('topics.txt','a+') as f:
            f.write(all_data)
            f.close()
        # for data in all_data['his']:
        #     try:
        #         if data not in self.topics_list:
        #             print data
        #             # filename = 'topics.txt'
        #             self.topics_list.append(data)
        #             self.flag += 1
        #             item['qid'] = self.flag
        #             dt_time = datetime.datetime.now()
        #             un_time = time.mktime(dt_time.timetuple())
        #             un_time = str(un_time)[:-2]
        #             print un_time
        #             url = 'https://m.baidu.com/his?callback=json&type=3&pic=1&net=1&hisdata=[{"kw":"'+data+'","time":'+un_time+'}]&_=1520988906089"'
        #             # item['answer'] = request.url
        #             item['re_answer'] = 'data'
        #             # with open(filename,'a+') as f:
        #             #     f.write(data)
        #             #     f.close()
        #             yield item
        #             yield self.make_requests_from_url(url)
        #     except Exception,e:
        #         pass