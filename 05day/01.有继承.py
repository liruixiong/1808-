class animal(object):
	def eat(self):
		print("吃")
	def fas(self):
		print("睡")
class cat(animal):
	pass
class dog(animal):
	pass

hsq = dog()
hsq.eat()
hsq.fas()
