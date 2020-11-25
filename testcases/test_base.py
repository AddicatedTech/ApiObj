#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 18:05
# @Author  : Addicated
# @Site    : 
# @File    : test_base.py
# @Software: PyCharm
from api.get_token import GetToken

class TestBase:

	def setup(self):
		# 但是这样发现 apiObj中的变量还是没有被封装起来，所以在apiObj中进行私有变量处设置
		# 是为了避免api对象的内部逻辑在外部可以被看到
		self.token = GetToken()
