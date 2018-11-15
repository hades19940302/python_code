#!/usr/bin/env python
# coding=utf-8
# author=hades
import threadpool as tp
import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def test():
	data = {
	'act':'reply',
	'mid':'4164151972842135',
	'cid':'4164152014897889',
	'uid':'6167846255',
	'forward':0,
	'isroot':0,
	'content':'回复@hades-pubg:[小黄人高兴]',
	'ouid':6167846255,
	'nick':'hades-pubg',
	'ispower':1,
	'status_owner_user':6167846255,
	'canUploadImage':1,
	'module':'scommlist',
	'dissDataFromFeed':'[object Object]',
	'root_comment_id':'4161738137925148',
	'approvalComment':'false',
	'location':'page_100505_single_weibo',
	'pdetail':'1005056167846255',
	'_t':0,
	}
	headers = {
		'Accept': '*/*',
	    'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN, zh;q=0.8',
		'Connection':'keep-alive',
		'Content-Length':'493',
		'Content-Type':'application/x-www-form-urlencoded',
		'Host':'weibo.com',
		'Origin':'https://weibo.com',
		'Referer':'https://weibo.com/pubghades/home?topnav=1&wvr=6',
		'User-Agent':'Mozilla/5.0(WindowsNT6.1;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/61.0.3163.100Safari/537.36',
		'X-Requested-With':'XMLHttpRequest',
		'Cookie':'SINAGLOBAL=9591043937900.918.1495591272180; a5787_times=1; uid=13ef1d22f52d931080a0f4d50be477c0; wb_cmtLike_6167846255=1; httpsupgrade_ab=SSL; wvr=6; TC-V5-G0=784f6a787212ec9cddcc6f4608a78097; SSOLoginState=1508290380; SCF=AsuhHiEzQ5pVKFsKV3kWPHZB2G46xXUsrOKD9JCyFavYbBdbJdMWuPyU5Oq5QgAof9c7uCRkkKABWup-BVTmIoM.; SUB=_2A2504t8cDeRhGeBP7VUZ9CjOzjmIHXVXmbfUrDV8PUNbmtAKLRH9kW9wIeXdCL1foIBQDkkezaSs1GEugg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhMrXBMS.7kur7eEzgrP2oh5JpX5KMhUgL.FoqpSoMRShqESK-2dJLoI7DQqgxLMEf7Ugir; SUHB=0TPlU6FRclHy0N; ALF=1539826378; TC-Page-G0=07e0932d682fda4e14f38fbcb20fac81; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=8335100059128.903.1508290383015; ULV=1508290383255:137:56:11:8335100059128.903.1508290383015:1508288833340; wb_cusLike_6167846255=Y',	
		}
	r = requests.post("https://weibo.com/aj/v6/comment/add?ajwvr=6&__rnd=1508295051256",data=data,headers=headers,verify=False)
	print  r.content
	pass
#每隔600秒执行一次
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(test,'cron',second='*/1000',hour='*')
    print 'Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C')
    try:
        scheduler.start()
    except KeyboardInterrupt,SystemExit:
        scheduler.shutdown()

