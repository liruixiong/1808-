import time
class dog():
	def __init__(self):
		self.age = 10
	def wark(self):
		print("嗷 嗷嗷")
class xtq(dog):
	def __int__(self):
		self.name = "哮天犬"
		super().__init__()
	def wark(self):
		for i in range(3):
			print("啊啊啊")
			time.sleep(1)
		super().wark()
xtq = xtq()
xtq.wark()

print(xtq.name)
