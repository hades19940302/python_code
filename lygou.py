#!/usr/bin/env python
# coding=utf-8
# author=ljs
# 捞月狗获取用户信息


import requests
import threadpool as tp

ids = []

for x in xrange(1000,2000):
	ids.append(x)
	pass
def test(arg_):
	r =requests.post("http://120.26.48.229:9081/usersvc/GetUserinfo", "{\"id\":%s}"%arg_)
	print r.content
	pass
pool = tp.ThreadPool(2)
reqs = tp.makeRequests(test, ids)
[pool.putRequest(req) for req in reqs]
pool.wait()

