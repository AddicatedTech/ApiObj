#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 13:27
# @Author  : Addicated
# @Site    : 
# @File    : test_get_token.py
# @Software: PyCharm
from string import Template

import requests
import yaml

from api.base_api import BaseApi


class GetToken(BaseApi):
	_corpid = "ww01499f8ea8a9861f"
	_corpsecret = "2fUo73u09VhsVhxvdb2ffCvWVkggPa52_KKx9cvXDxA"

	# 定义操作yaml内部数据进行模板替换的方法
	#  之后tempalte替换方法可以封装到BaseApi中，方便各个apiObj进行调用
	def template(self):
		# 读取yaml文件，拿到返回值
		with open("../api/get_token.yaml") as f:
			# 同时 substitute 也可以传字典格式的参数
			data = {
				"corpid": self._corpid,
				"corpsecret": self._corpsecret
			}
			# re = Template(f.read()).substitute(corpid=self._corpid, corpsecret=self._corpsecret)
			re = Template(f.read()).substitute(data)
		# 当前进行转换后是字符串，所以调用yaml方法转换成python可操作的对象
		return yaml.safe_load(re)

	def get_token(self):
		# req = {
		# 	"method": "get",
		# 	"url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
		# 	"params": {
		# 		"corpid": self._corpid,
		# 		"corpsecret": self._corpsecret
		# 	}
		# }
		# req = yaml.safe_load(open("../api/get_token.yaml"))
		req = self.template()
		r = self.request_http(req)
		print(r.json())
		return r
