class home():
	def __init__(self,name,area):
		self.name = name
		self.area = area
		self.list = []
	def __str__(self):
		msg = "我的家在%s面积是%d床有%d"%(self.name,self.area,len(self.list))
		return msg
	def ban(self,jiaju):
		all = 0
		for bed in self.list:
			all+=bed.area
		diff = self.area - all
		print("剩余%s"%diff)
		if diff >= jiaju.area:
			self.list.append(jiaju)
		else:
			print("不够了")

class jiaju():
	def __init__(self,name,area):
		self.name = name
		self.area = area



lxl = home("北京长安街666号",1500)
bed = jiaju("席梦思",50)
for i in range(35):
	lxl.ban(bed)
print(lxl)
