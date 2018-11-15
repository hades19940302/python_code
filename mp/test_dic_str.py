#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/7/16 15:54


def test():
	allowed_address_pair = []
	s = ("8.8.8.8:2:22:22:22,9.9.9.9:33.22.222.33,").encode('ascii').split(',')
	s_tt = "'ip':'8.8.8.8','mac':'ff:ff:ff:ff',"
	s_sb = ("{'ip_address':'172.28.218.197','mac_address':'00:1b:24:f0:37:95'} {'ip_address':'172.28.218.198','mac_address':'00:1b:24:f0:37:99'}").split(' ')
	for item in s_sb:
		allowed_address_pair.append(eval(item))

	print(allowed_address_pair)

test()
