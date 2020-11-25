#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 11:38
# @Author  : Addicated
# @Site    : 
# @File    : test_yaml.py
# @Software: PyCharm
import yaml

def test_yaml():
	env = {
		"default": "dev",
		"testing_studio":
			{"dev": "127.0.0.1",
			 "test": "127.0.0.2"}
	}
	with open("env.yaml","w") as f:
		yaml.safe_dump(env,stream=f)


if __name__ == '__main__':
    test_yaml()