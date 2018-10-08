class Animal():
	def eat(self):
		print("吃")
class Cat(Animal):
	def eat(self):
		print("吃老鼠")
class Dog(Animal):
	def eat(self):
		print("吃肉")
def common_eat(animal):
	animal.eat()

dog = Dog()#多态这种行为一定基于继承和重写
cat = Cat()
common_eat(dog)
common_eat(cat)
