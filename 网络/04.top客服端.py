from socket import * 

s = socket(AF_INET,SOCK_STREAM)

s.bind(('',8800))

s.listen(5)

s1,add = s.accept()

msg = s1.recv(1024)
print(msg.decode('gb2312'))
s1.send('哈哈'.encode('gb2312'))

s1.close()
s.close()
