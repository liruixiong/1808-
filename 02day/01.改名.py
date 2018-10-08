import os
name = input("请输入文件名:")
fos = os.listdir(name)
os.chdir(name)
for i in fos:
	print(i)
	p = i.rfind(".")
	a = i[:p]
	s = i[p:]
	mi = a+"行动"+s
	os.rename(i,mi)
