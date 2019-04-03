#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 10:17
# @Author  : liyq23
# @Email   : liyq23@lenovo.com
# @File    : server.py


from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('',8000,application)

print "server http on port 8000"
httpd.serve_forever()