#!/usr/bin/env python
# coding=utf-8

class Trick(object):
	"""docstring for Trick"""
	def __init__(self, arg):
		super(Trick, self).__init__()
		self.arg = arg
		
class FlyToSky(object):
    pass

pw = type('Trick', (FlyToSky, ), {'laugh_at': 'hahahaha'})
# print pw().laugh_at
# print pw.__dict__
# print pw.__bases__
# print pw().__class__
# print pw().__class__.__class__

trick = Trick
# print type('trick', (), {})()

# print type('Trick', (), {})


class FlyToSky(object):
    pass

pw = type('Trick', (FlyToSky, ), {'laugh_at': 'hahahaha'})
print pw().laugh_at
print pw.__dict__
print pw.__bases__
print pw().__class__
print pw().__class__.__class__


