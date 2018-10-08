class tx():
	def __vip(self):
		print("开通会员成功")
	def open(self,money):
		if money > 10:
			self.__vip()
		else:
			print("余额不足")
qian = int(input("请输入充值金额："))
qq = tx()
qq.open(qian)
