#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 8:20
# @Author  : Addicated
# @Site    : ${SITE}
# @File    : test_test_request.py
from unittest import TestCase
from secrect_apiTest import test_request


# @Software: PyCharm
class TestApiRequest(TestCase):
	req_data = {
		"method": "get",
		"url": "http://127.0.0.1:9999/demo.txt",
		"headers": None,
		"encoding": "base64"
	}

	def test_send(self):
		ar = test_request.ApiRequest()
		print(ar.send(self.req_data))