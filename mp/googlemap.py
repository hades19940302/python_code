#!/usr/bin/env python
# coding=utf-8
# author=ntwu
import threadpool as tp
import requests
import json

def test(address):
	r = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address=%s'%address)
	data = json.loads(r.content)
	results = data['results'][0]

	geometry = results['geometry']
	location = geometry['location']
	lat = location['lat']
	lng = location['lng']
	formatted_address = results['formatted_address']
	return  lat,lng,formatted_address

t = test('LA')
print(t)