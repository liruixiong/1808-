class Dog(object):
	__instance = None#类属性 用来保存对象
	__flag = True #默认第一次
	def __init__(self,name):
		if Dog.__flag:
			self.name = name
			Dog.__flag = False

	def __new__(cls,*ares,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)#把对象保存起来
			return cls.__instance
		else:
			#把保存的对象之间返回 不需要创建
			return cls.__instance
dog = Dog("小红")

dog1 = Dog("小米")

print(id(dog))
print(id(dog1))
print(dog.name)
print(dog1.name)
