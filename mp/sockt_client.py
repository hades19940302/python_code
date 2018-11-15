#!/usr/bin/env python

import socket 


host,port = '192.168.0.105',9001

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect((host,port))


while True:
		
		
	user_input=raw_input("msg send to server::").strip()
	if len(user_input)==0:
		continue
	c.send(user_input)
		
	return_data = c.recv(1024)
		
	print 'recved ',return_data
		
		
c.close()