#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 8:56
# @Author  : Addicated
# @Site    : ${SITE}
# @File    : test_test_env.py
from unittest import TestCase
from env_test import test_env
# @Software: PyCharm


class TestApi(TestCase):
	data = {
		"method": "get",
		"url": "http://testing-studio:9999/demo.txt",
		"headers": None

	}
	def test_send(self):
		api =test_env.Api()
		print(api.send(self.data).text)