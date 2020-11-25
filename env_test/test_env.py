import requests
import yaml


# 多环境下的接口测试解决方案
# 在请求之前，对请求的url进行替换
# 1 需要二次封装requests，对请求进行定制化
# 2 将请求的结构体的url从一个写死的ip地址改为一个 任意的域名
# 3 使用一个env配置文件，存放各个环境的配置信息
# 4 然后将请求结构体中的url替换为 env 配置文件中个人选择的url
# 5 将env配置文件用yaml进行管理
class Api:
	env = yaml.safe_load(open("env.yaml"))

	# data 是一个请求的信息
	def send(self, data: dict):
		# 请求之前对url进行替换，  并且测试环境一并参数化，实现修改配置文件可以直接驱动不同环境测试
		data["url"] = str(data["url"]).replace("testing-studio", self.env["testing_studio"]
		[self.env["default"]])

		r = requests.request(method=data["method"], url=data["url"], headers=data["headers"], )
		return r
