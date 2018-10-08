from threading import Thread

from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',8080))

ip = input("请输入对方IP地址：")
port = int(input('请输入对方端口：'))
def send():
	while True:
		content = input("请输入发送内容：")
		s.sendto(content.encode('gb2321'),(ip,port))

def recv():
	while True:
		msg = s.recvfrom(1024)
		print(msg[0].decode('gb2312'))


t1 = Thread(target=send)
t2 = Thread(target=recv)
t1.start()
t2.start()
t1.join()
t2.join()
