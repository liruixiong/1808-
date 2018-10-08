class xouji():
	def __init__(self):
		self.box = []
	def xou(self):
		print("欢迎来到学籍管理系统".center(30,"*"))
		while True:
			print("1、录入")
			print("2、修改")
			print("3、查找")
			print("4、删除")
			print("5、保存")
			print("6、退出")
			num = int(input("请选择功能"))
			if num == 1:
				self.yi()
			elif num == 2:
				self.er()
			elif num ==3:
				self.an()
			elif num == 4:
				self.si()
			elif num == 5:
				self.wu()
			elif num == 6:
				self.lui()
	def yi(self):
		xjb = {}
		name = input("请输入学生名字")
		age = input("请输入年龄")
		sex = input("请输入性别")
		phone = input("请输入手机号")
		xjb["name"] = name
		xjb["age"] = age
		xjb["sex"] = sex
		xjb["phone"] = phone
		self.box.append(xjb)
		print(self.box)
	def er(self):
		name = input("请输入要修改学生的名字")
		for xjb in self.box:
			if xjb["name"] == name:
				print("1、修改名字")
				print("2、修改年龄")
				print("3、修改性别")
				print("4、修改手机号")
				num = int(input("请选择修改功能"))
				if num == 1:
					name = input("请输入新的名字")
					xjb["name"] = name
				elif num == 2:
					age = input("请输入新的年龄")
					xjb["age"] = age 
				elif num == 3:
					sex = input("请输入新的性别")
					xjb["sex"] = sex
				elif num == 4:
					phone = input("请输入新的手机")
					xjb["phone"] = phone
				print("修改")
				break
	def san(self):
		print("查找")
		name = input("请输入你要查找的学生姓名")
		for xjb in self.ox:
			if xjb["name"] == name:
				print("姓名\t年龄\t性别\t手机号")
				print("%s\t%s\t%s\t%s"%(xjb["name"],xjb["age"],xjb["sex"],xjb["phone"]))
				break
	def si(self):
		print("删除")
		name = input("请输入你要删除的学生姓名")
		for xjb in self.box:
			if xjb["name"] == name:
				num = int(input("是否要删除 1:Yes 2:No"))
				if num == 1:
					self.box.remove(xjb)
				break
	def wu(self):
		print(type(list))
		u = str(list)
		print(u)
		f= open("名单.txt","w")
		f.write(u)
		f.read()
		f.close
				
	def lui(self):
		print("退出")
		exit()

x = xouji()
x.xou()








