class animal(object):
	def __init__(self):
		self.__age = 12138
	def getAge(self):
		return self.__age
class dog():
	pass
hsq = dog()

print(hsq.getAge())
