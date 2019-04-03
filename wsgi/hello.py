#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 10:18
# @Author  : liyq23
# @Email   : liyq23@lenovo.com
# @File    : application.py


def application(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return '<hi>hello,web</h1>'