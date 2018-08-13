#!/usr/bin/env python
# coding=utf-8
# author=f

import scrapy
import json

from weipai.items import WeipaiItem

class weipai_spider(scrapy.Spider):
    allowd_domains = ["http://w1.weipai.cn/"]
    start_urls = ["http://w1.weipai.cn/user_fans_list?count=1000&relative=after&uid=50f8ff597f3494a702000066"]

    uid_list = []
    def parse(self, response):
        item = WeipaiItem()
        all_data = json.loads(response.body)
        for id in all_data['user_list']:
            try:
                if id['user_id'] not in self.uid_list:
                    self.uid_list.append(id['user_id'])
                    item['user_id'] = id['user_id']
                    item['url'] = "http://IP/user_fans_list?count=1000&relative=after&uid=%s"%id['user_id']
                    yield item
                    yield self.make_requests_from_url(item['url'])
            except Exception,e:
                pass