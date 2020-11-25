#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 16:33
# @Author  : Addicated
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

data = ('{"poHeaderDto":{"attribute10":"ODM_SERVER"}}',)

# print(type(data[0]))
print(type(data))
print(data[0])
'''
python 常用的标准库
操作系统相关 os
时间与日期相关  time ，datetime
科学计算   math
网络请求  urllib

os 模块主要对文件，目录的操作
常用方法：
	os.mkdir() 创建目录
	os.removedirs() 删除文件
	os.getcwd() 获得当前目录
	os.path.exists(dir or file) 判断文件或者目录是否存在

'''
import  os
print(os.getcwd())

import time
print(time.time())
print(time.localtime())
# 格式化获得当前时间的做法
print(time.strftime("%Y年%m月%d %H:%M:%S",time.localtime()))

# 获取两天前的时间
two_day_before= time.time() - 60*60*24*2
time_stamp = time.localtime(two_day_before)
print(time.strftime("%Y年%m月%d %H:%M:%S",time_stamp))


# math
# math.celi(x) 返回大于等于参数x的最小整数
# math.floor(x) 返回小于等于参数x的最大整数
# math.sqrt(x) 平方根

# unittest测试框架
# 单元测试概述
# unittest框架介绍
# unittest实战

# 单元测试什么时候测试，一般来说越早越好，越早进行，后期进行集成测试时错误越少
# 单元测试需要注意的点
# 大前提要知道被测程序的输入和输出，
# 基于预期和程序逻辑来写case而不是基于程序的逻辑来写case

# 单元测试覆盖率
# 代码覆盖率也被用于自动化测试和手工测试来度量测试是否全面的指标之一
# 应用覆盖率的思想增强测试用例的设计
# 单元测试覆盖类型
# 语句覆盖
	# 通过设计一定量的测试用例，保证被测试的方法每一行代码都会被执行一遍
	# 运行测试用例的时候被击中的代码就称为被覆盖的语句
	# 语句覆盖      是一个最基础的覆盖方式，但是也是最薄弱的，如果完全依赖语句覆盖
	# 会出现很严重的问题

# 条件覆盖
	# 条件覆盖和判定覆盖类似，不过判定覆盖关注整个判定语句，而条件覆盖则关注某个判断条件
	# 针对的是条件设计而非判定 真假的设计
	# 缺陷就是 测试用例指数级增加

# 判断覆盖
	# 运行测试用例的过程中被击中的判定语句
	# 漏洞
	# 大部分的判定语句是由多个逻辑条件组合而成，若仅仅判断其整个最终结果
	# 而忽略每个条件的取值情况，必然会遗漏部分测试路径
	# ex
	# 对于判断条件，假如有两个if语句
	# 要设计的case就有  TT,FF,TF,FT 四种情况

# 路径覆盖
	# 覆盖所有可能执行的路径
	# 比如根据 是 否 来进行设计

# unittest框架介绍
# python自带的单元测试框架，常用在单元测试
# 在自动化测试中提供用例组织与执行
# 提供丰富的断言方法-验证函数等功能
# 加上HTMLTestRunner可以生成 html报告

# unittest提供了test cases ，test suites ，test fixtures，test runner相关的组件
# 编写规范
	# 测试模块首先 import unittest
	# 测试类必须继承unittest.TestCase
	# 测试方法必须以 test_开头
	# 模块名字，类名没有特殊要求

# 测试框架架构
# setUp 用来测试准备环境 tearDown用来清理环境
# 如果想要在所有case执行之前准备一次环境，并且在所有case执行结束后再清理环境
# 可以使用setUpClass 和 tearDownClass 比如数据库的连接与销毁
# 不想执行可以 @unittest.skip
# 测试方法的命名 以 test开头

# pytest介绍
# pip install pytest-suger 显示测试进度条
# pip install pytest-rerunfailures 失败用例重复运行
# pip install pytest-xdist   多cpu分发
# pip install pytest-assume  添加断言
# pip install pytest-html    生成一个html的结果报告
# pip list 查看
# pytest -h 帮助

# pytest --reruns 3 # 失败用例重复执行3次
# pytest.assume(断言表达式)  # 即使失败也会继续向下运行
# conftest 里面存放@fixture修饰的用例就可以直接使用
# conftest.py配置须知
# 名字不能更换
# conftest.py 与运行的用例要在同一个package下，并且有init文件
# 不需要import导入conftest文件，pytest会自动查找
# 全局的配置和前置工作都可以写在这个py文件下
# pytest.mark

# 多线程并行与分布式执行
# pytest 分布式执行插件 pytest-xdist 多个cpu或者主机执行，前提，用例之间都是独立的
# 没有先后顺序，随机都能执行，可重复运行不影响其他用例。
# pip install pytest-xdist
# 多个cpu并行执行用例， 直接加 -n 3 并行数量  pytest -n 3
# 在多个终端下一起执行

# pytest参数化
# @pytest.mark.parametrize(argnames,argvalues)
# argnames 要参数化的变量，string(逗号进行分割）,list,tuple
# argvalues 参数化的值，list，list[tuple]
