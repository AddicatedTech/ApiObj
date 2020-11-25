# 接口测试封装思想
* 配置
    根据配置文件获取初始配置和依赖
* 接口封装  霍格成为 api object
    封装接口调用进行抽象封装
    类似PO效果
* 业务流程
    数据初始化
    业务用例设计，含有多个api形成的流程定义，不要在包含任何接口实现细节
    断言
# 接口测试框架构成
- API对象          完成对接口的封装
   * 架构设计
       多协议支持，http，tcp thrft 等需要不同的底层引擎
       保证用例的协议无关，基于接口或者抽象实现
       多环境的支持
       * 架构管理
       package管理业务模块
       class管理业务功能
       method完成业务具体行为
       配置文件读取初始配置
       使用继承规划用例执行顺序
       使用testcase完成测试用例落地
       使用assertion完成业务正确性校验
       使用数据文件管理用例的数据驱动
       使用jenkins完成持续集成
   * 实现
        code方式 输出=业务.功能（输入)
        配置文件方式  yaml格式，json格式
- 接口测试框架      完成对api的驱动
- 配置模块          完成对配置文件的读取
- 数据封装         数据构造与测试用例的数据封装
- utils           其他功能封装，改进原生框架不足
- 测试用例         调用API对象实现业务并断言

# 选择语言 选择与开发相同的编程语言和技术栈
- python
* 选择合适的测试框架
py + request + pytest + allure2 


# 加密接口处理方案
# 原理
# 在得到响应后对响应做解密处理
# 1 如果知道使用的是哪个通用加密算法的话可以自行解决
# 2 如果不了解对应的加密算法，可以让开发提供加解密的lib
# 3 如果既不是通用加密算法，研发也无法提供加解密的lib的话
# 可以让加密方提供远程解析服务，这样保证算法仍然是解密(可能在外包中常用此方式)

# ex 应对base64 加密的接口，
#  1 调用python自带的base64库。直接对返回的相应做解密，即可得到解密后的相应
#  2 封装对不同算法的处理方法

# 多环境下的接口测试解决方案
# 在请求之前，对请求的url进行替换
# 1 需要二次封装requests，对请求进行定制化
# 2 将请求的结构体的url从一个写死的ip地址改为一个 任意的域名 
# 3 使用一个env配置文件，存放各个环境的配置信息
# 4 然后将请求结构体中的url替换为 env 配置文件中个人选择的url
# 5 将env配置文件用yaml进行管理


# apiObject 引入
# 传统case存在的问题
# 高耦合性
# 可维护性差
# apiobject 思想与 po相通
# 隔离变与不变的内容
# 接口细节和业务进行抽离
# apiobject原则
# 每个公共方法代表接口锁提供功能
# 不暴露api内部细节
# 不在接口实现层写断言
# 每个method返回其他的apiobject或者用来做断言
# 不需要对每个api都进行实现


# 
corpid  ww01499f8ea8a9861f
corpsecret  2fUo73u09VhsVhxvdb2ffCvWVkggPa52_KKx9cvXDxA

# 通用接口协议的封装
# 关于http请求的二次封装
# BaseApi  概念其实有点类似于 po中的basepage 
# 作为其他api的一个父类，其他的api直接对其进行继承
# 实现原理
# 吧发起的请求信息转化为一个字典结构体
# 直接使用puython 关键字传参的方式，将请求结构体传给request.request方法

# 接口自动化中的测试步骤数据驱动化
# 前面对于请求体的字典格式化，通过requests.request方法进行调用的形式
# req请求体数据就是测试步骤
# 前提（不必要）
# 请求信息是一个字典结构体
# 步骤
# 1 ，使用yaml文件对测试步骤进行数据驱动
# 2 ，在yaml文件中实现变量传递  需要使用到模板技术
# 模板字符串 string.Template
# 模板字符串支持 基于 $的替换

# 测试数据的数据驱动
# 提高数据的可维护性
# 规范化数据管理
# 可对数据进行备份
# pytest.paramtize注解

# 配置的数据驱动

# 共通的case抽取
# 创建一个TestBase类
# TestBase 存放共用的方法，
# 诸如 前后置 ，数据库连接等方法
# 其他的case都继承与TestBase

# 总结
# api object模式
# 数据驱动
#      测试步骤
#       测试数据
#       测试配置
# 其他
#       基于加密接口的测试用例设计
#       多环境下的接口测试
#       通用测试用例的封装

# ----------11.13 深夜
# 复杂数据解析
# 数据保存：将复杂的xml或者json请求体保存到文件模板中
# 数据处理
# 使用mustache，freemaker等工具解析
# 简单字符串替换  string.Template库
# 使用json xml api 进行结构化解析
# 数据生成，输出最终结果

# 基于json的模板技术 mustache
# python中对应的苦为 pystache
# 具体使用方法是在结构体中使用{{变量名}} 括起来的数据都能够进行替换
# 使用 
# import pystache
# pytache.render({"person":"要替换的值")

# xml请求
# requests库中没有针对xml结构请求体接口的封装
# 所以在需要测试xml作为结构体的接口的时候
# 需要额外的配置 请求头  headers={"Content-Type":"application/xml"}
# 之后正常通过结构化数据 调用requests.request()方法传参即可

# 断言框架 hamcrest


# OWSAP 安全测试体系
# 主要聚焦于测试工程师需要掌握的安全技能
# 移动端安全
# 服务端安全

2020 年 11.14 测试开发 20-40k jd整理
前端，数据存储，和文件系统
spring mybaits 扎实java基础 测试平台开发能力，全栈开发
CI CD，测试覆盖率 
dubbo接口 ，
测试工具开发 
服务端接口测试，服务化架构测试经验
白盒
flask
docker，linux，appium
大数据处理工具，压测工具
常用中间件
ssm框架
APITest
测试左移，测试右移，分布式

jenkins api----2020.11.14
# jenkins 对外暴露的动作交互入口
# 为外部程序提供入口，可以控制jenkins
# 支持协议 http
# api 接口支持用户名，密码认证
# api支持的典型功能，运行job  查看任务状态，返回任务号

# jenkins api环境准备
# 创建一个有任务运行和状态查询权限的用户
# 准备一个打算通过api远程控制的任务
# 较老版本的jenkins关闭跨站脚本伪造请求保护，新的采取Crumb

# 远程调用 Jenkins API启动任务
# 人物名  first job
# 远程api服务地址  http://ip:8080/job.first_job/build
# 请求方法 post
# 用户名，密码添加方法   username:password@hostname:port
# 运行期望结果
# 任务启动
# 服务返回http status 201