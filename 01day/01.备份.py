name = input("请输入名字：")
f = open(name,'r')
content = f.read()

p = name.rfind(".")
s = name[:p]
e = name[p:]
nome = s + '备份' + e
f1 = open(nome,"w")
f1.write(content)
f.close()
f1.close()
