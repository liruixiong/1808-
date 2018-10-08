from socket import *
#创建
s = socket(AF_INET,SOCK_DGRAM)

s.sendto("弟弟".encode('gb2312'),('192.168.43.95',8080))
while True:
	msg = s.recvfrom(1024)
	print(msg[0].decode('gb2312'),msg[1][0])
s.close()
