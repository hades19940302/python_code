# -*- coding: utf-8 -*-
# @Author: hades
# @Date:   2017-10-03 15:13:15
# @Last Modified by:   hades
# @Last Modified time: 2017-10-03 15:51:35
import threadpool as tp
import requests
import json


datas = []
for i in range(17924334,17999999):
	datas.append(i)

def test(arg_):
    r = requests.get("http://t.cn/R0dLnPN?m=4158553289353227&u=6167846255")
    print r.status_code

pool = tp.ThreadPool(20)
reqs = tp.makeRequests(test, datas)
[pool.putRequest(req) for req in reqs]
pool.wait()
