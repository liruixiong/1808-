class Animal():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def eat(self):
		print("吃")
	def sleep(self):
		print("睡")
	def __str__(self):
		msg = "名字：%s  年龄：%d"%(self.name,self.age)
		return msg
	
class A(Animal):
	def test(self):
		print("看电影")
class B(Animal):
	def tese1(self):
		print("听音乐")

b = A("斌哥",25)	
print(b)
b.eat()
b.sleep()
b.test()

d = B("源哥",25)	
print(d)
d.eat()
d.sleep()
d.tese1()
