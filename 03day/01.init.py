class cat():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("吃饭")
	def sleep(self):
		print("睡觉")
	def oll(self):
		print("打豆豆")
	def intriduce(self):
		print("我叫%s,年龄%d"%(self.name,self.age))
	def __str__(self):
		msg = "我叫%s 年龄%d"%(self.name,self.age)
		return msg

tom = cat("都比",12)
tom.sleep()
tom.oll()
#tom.intriduce()
print(tom)

