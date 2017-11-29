'''
  Socket 网络编程
'''
'''
  计算机之间怎么实现通讯
    发 send
    收 receive
'''
'''
  一个机器最多开65535个 port
    ip 地址相当于总机
    分机号就相当于是
'''
# 客户端
import socket

client = socket.socket()  # 申明Socket 类型 同时生成socket 链接对象

client.connect(('localhost', 6969))

while True:
  msg = input('>>:').strip()
  if len(msg) == 0: continue
  # 只能发送bytes类型 bytes 只能接受ASCII
  # client.send('我要下载a片'.encode('utf-8'))
  client.send(msg.encode('utf-8'))
  data = client.recv(1024)
  print("recv:", data.decode('utf-8'))

client.close()
