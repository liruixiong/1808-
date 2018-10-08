from socket import *
#创建一个udp的套接
s = socket(AF_INET,SOCK_DGRAM)
bindAddr = ('',8080)
s.sendto("弟弟".encode('gb2312'),('192.168.43.80',8080))
while True:
	msg = s.recvfrom(1024)
	print(msg[0].decode('gb2312'),msg[1][0])
s.close()
