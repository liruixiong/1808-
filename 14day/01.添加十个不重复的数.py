import random
class Shu():
	list = []
	@classmethod
	def shu(cls):
		while True:
			num = random.randint(1,100)

			if num not in cls.list:
				cls.list.append(num)
			if len(cls.list) == 10:
				break
		return cls.list
l = Shu.shu()
print(l)
