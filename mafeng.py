#!/usr/bin/env python
# coding=utf-8
# author=hades
# mafeng
import requests
import json


def test():
	r = requests.get('https://mapi.mafengwo.cn/wenda/list/get_qa_list/v5?app_code=cn.mafengwo.www&app_ver=8.1.7&channel_id=App%20Store&device_token=e9347d10d20d4834786a45faf6b7e46de03438bba723b3e7c5fac7b18265fe42&device_type=ios&hardware_model=iPhone10%2C3&idfa=43325295-7453-484B-9619-C81D5399639D&idfv=BFD9573F-500B-4622-B50F-9FFBD730D8A0&jsondata=%7B%22page%22%3A%7B%7D%2C%22mdd_id%22%3A%2210183%22%2C%22filter_type%22%3A%22all%22%7D&mfwsdk_ver=20160401&o_lat=38.888954&o_lng=121.534488&oauth_consumer_key=4&oauth_nonce=3a97dcc0-c43e-42d9-bbbb-e5fe89b88e25&oauth_signature=XdXMSwMBy1exmG4N1WS1dEDrViw%3D&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1521536217&oauth_token=0_d5af5e71fbcea723b6af2ddae8ab084a&oauth_version=1.0&open_udid=BFD9573F-500B-4622-B50F-9FFBD730D8A0&screen_height=2436&screen_scale=3&screen_width=1125&sys_ver=11.2.5&time_offset=480&x_auth_mode=client_auth')
	json_data = json.loads(r.content)
	data = json_data['data']
	list_ = data['list'] 
	print(list_)

test()