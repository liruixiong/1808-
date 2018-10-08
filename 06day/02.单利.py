class Dog(object):
	__instance = None
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)#把对象保存起来
			return cls.__instance
		else:
			#把保存的对象之间返回 不需要创建
			return cls.__instance
dog = Dog()
print(id(dog))
dog1 = Dog()
print(id(dog1))
