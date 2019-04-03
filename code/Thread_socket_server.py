#!/usr/bin/env python


import SocketServer
import commands,time



class MySocktServer(SocketServer.BaseRequestHandler):
	
	
	def handle(self):
		print 'Got a new conn',self.client_address
		while True:
			cmd_ = self.request.recv(1024)
			if not cmd:
				print 'Lost conn from ' ,self.client_address
				break
			#print 'recv :',data
			cmd_result =  	commands.getstatusoutput(cmd)
			time.sleep(0.2)
			
			
			
			self.request.send(data.upper(cmd_result[1]))
			
			
if __name__=='__main__':
	h='0.0.0.0'
	p=9001
	s = SocketServer.ThreadingTCPServer((h,p),MySocktServer)
	s.serve_forever()