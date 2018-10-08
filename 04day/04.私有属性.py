class person():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.__mimi = "苏伟苏伟 哦 苏威"
	def __str__(self):
		msg = "我叫%s,我家里有%s座矿"%(self.name,self.age)
		return msg
	def getMi(self):
		return self.__mimi
	def getMoney(self):
		return self.__haha
lz = person("小源",1000)
print(lz)
print(lz.getMi())

		
