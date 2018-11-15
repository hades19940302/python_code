#!/usr/bin/env python

id_list = []
def test():
	with open('baiduzhidao_url_list_3.txt','rb') as f:
		for line in f.readlines():

			id_ = line[33:-7]
			if id_ not in id_list:
				id_list.append(id_)
				f1 = open('baiduzhidao_ids.txt','a+')
				f1.write(id_+'\n')
				f1.close()
			else:
				pass

test()