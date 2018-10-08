import time
print("欢迎来到车辆销售中心".center(30,"*"))
box = []
while True:
	print("1.登记车辆")
	print("2.修改内容")
	print("3.查找车辆")
	print("4.删除车辆")
	print("5.存档")
	print("6.退出系统")
	num = int(input("请选择功能："))
	if num == 1:
		xjb = {}
		name = input("请输入品牌：")
		age = input("请输入价格：")
		xjb["name"] = name
		xjb["age"] = age
		box.append(xjb)
		print(box)
	elif num == 2:
		nam = input("请输入要修改的品牌：")
		for xjb in box:
			if xjb["name"] == nam:
				print("1.修改品牌")
				print("2.修改价格")
				nu = int(input("请选择修改功能："))
				if nu == 1:
					name = input("请输入新的名称：")
					xjb["name"] = name
				elif nu == 2:
					age = input("请输入新的价格：")
					xjb["age"] = age
				break
	elif num ==  3:
		name = input("请输入要查找的品牌：")
		flag = False
		for xjb in box:
			if xjb["name"] == name:
				print("姓名\t年龄")
				print("%s\t%s\t"%(xjb["name"],xjb["age"]))
				flag = True
				break
		if flag == False:
			print("没有这辆车")
	elif num == 4:
		name = input("请输入你要删除的品牌：")
		flag = False
		for xjb in box:
			if xjb["name"] == name:
				ui = int(input("是否要删除 1:yes  2:No  :"))
				if ui == 1:
					box.remove(xjb)
					print("删除成功")
				flag = True
				break
		if flag == False:
			print("没有这辆车")
	elif num == 5:
		print(type(box))
		u = str(box)
		print(u)
		f = open("存档.txt","a+")
		f.write(u)
		f.close()
	elif num == 6:
		qw = int(input("是否退出系统 1.yes 2.No :"))
		if qw == 1:
			for i in range(3):
				print("关闭中")
				time.sleep(1)
			break
		elif qw == 2:
			for i in range(3):
				print("恢复中")
		time.sleep(1)
