#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 13:51
# @Author  : Addicated
# @Site    : 
# @File    : test_get_token.py
# @Software: PyCharm

# testcases 是以pytest为测试框架  一个method 就是一个case
from jedi.plugins import pytest

from testcases.test_base import TestBase


class TestToken(TestBase):
	# 在这里面调用api下封装好的接口对象

	def test_get_token(self):
		assert self.token.get_token().json()["errcode"] == 0
