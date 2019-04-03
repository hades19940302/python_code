#!/usr/bin/env python
# coding=utf-8

import eventlet
from eventlet import wsgi
 
 
class AnimalApplication(object):
    def __init__(self):
        pass
 
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return ['This is a animal applicaltion!rn']
 
 
if '__main__' == __name__:
    application = AnimalApplication()
    wsgi.server(eventlet.listen(('', 8080)), application)