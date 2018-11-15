#!/usr/bin/env python
# coding=utf-8
# author=ntwu
import threadpool as tp
import requests
import json

ids = []

for i in range(2000):
	ids.append(i)

def test(arg_):
	r = requests.get("http://www.csinla.com/api/posts/%s/"%arg_)
	print r.content
	print arg_


pool = tp.ThreadPool(2)
reqs = tp.makeRequests(test, ids)
[pool.putRequest(req) for req in reqs]
pool.wait()
