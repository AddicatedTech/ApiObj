#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:30
# @Author  : Addicated
# @Site    : 
# @File    : base_api.py
# @Software: PyCharm

#
import requests


class BaseApi:

	def request_http(self, req):
		# 解包键值对应传参
		r = requests.request(**req)
		return r

	# 在这里面很尽兴定义适用于各种协议的请求方法，以req为参数
	def request_dubbo(self, req):
		# 假如之后需要进行其他格式的接口定义
		pass
