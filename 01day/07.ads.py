name = input("请输入文件名：")
f = open(name,"r")
co = f.read()
p = name.rfind(".")
s = name[:p]
e = name[p:]
ne = s+"备份"+e
f1 = open(ne,"w")
f1.write(co)
f.close()
f1.close()
