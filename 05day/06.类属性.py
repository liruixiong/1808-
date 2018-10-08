class Dog():
	print("哈哈哈")
	count = 0#类公有属性
	__a = 1000#类私有属性
	def __init__(self):
		self.name = "老王"#共有属性 实例属性
		self.__age__ = 100#实例私有属性
		Dog.count +=1
	def eat(self):#公有方法 实例方法
		print("吃")

	def __test(self):#私有方法
		print("私有方法")

	@classmethod
	def getA(cls):#类方法 cls = Dog
		return cls.count
	@classmethod
	def setA (cls,count):
		cls.count = count
	@classmethod
	def __show(cls):
		print("啊啊啊")
	@classmethod
	def show(cls):
		cls.__show()
dog = Dog()
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()
print(dog.count)#用对象访问类属性
print(dog.count)#用访问类属性
#print(Dog.__a)
Dog.setA(10)#通过共有类方法设置值
print(Dog.getA())#用类访问方法
print(dog.getA())#用对象访问类方法
#print(Dog.__show())#不能访问私有
Dog.show()#通过公有类方法 访问私有类方法
