# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhidaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TopicItem(scrapy.Item):
    qid = scrapy.Field()
    # answer = scrapy.Field()
    re_answer = scrapy.Field()

class OsshieteItem(scrapy.Item):
    qid = scrapy.Field()
    answer = scrapy.Field()
    question = scrapy.Field()
    question_detail = scrapy.Field()

class qaItem(scrapy.Item):
    t = scrapy.Field() # 正例
    qid = scrapy.Field() # 唯一索引
    question = scrapy.Field() # 问题
    answer = scrapy.Field() # 答案
    bingo = scrapy.Field() # 是否为最佳
    like = scrapy.Field() # 点赞

class qqItem(scrapy.Item):
    t = scrapy.Field() # 正例
    qid = scrapy.Field() # 唯一索引
    question = scrapy.Field() # 问题
    re_question = scrapy.Field() #相似问题