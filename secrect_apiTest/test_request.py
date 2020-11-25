#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 8:02
# @Author  : Addicated
# @Site    : 
# @File    : test_request.py
# @Software: PyCharm
import requests
import json
import base64


#
# def test_encode():
# 	url = "http://127.0.0.1:9999/demo.txt"
# 	r = requests.get(url=url)
# 	result = json.loads(base64.b64decode(r.content))
# 	print(result)
#
#
# if __name__ == '__main__':
# 	test_encode()


class ApiRequest:
	def send(self, data: dict):
		res = requests.request(data["method"], data["url"], headers=data["headers"])
		if data["encoding"] == "base64":
			return json.loads(base64.b64decode(res.content))


		# 加密后的响应值发给第三方，让第三方去做解密
		elif data["encoding"] == "private":
			# 返回的是解密的信息
			return requests.post("url", data=res.content)
