# 服务器端
import socket

server = socket.socket()
server.bind(('localhost', 6969))  # 绑定要监听的端口
server.listen()  # 监听  listen(5) 最多挂起几个链接
print('我要开始等电话了')
# 返回两个字  链接实例, 对方地址
# conn就是客户端连过来而在服务端为生成的链接实例
conn, addr = server.accept()  # 等电话打进来
while True:
  # print(conn, addr)
  print('电话来了')
  data = conn.recv(1024)

  print('recv:', data)
  conn.send(data.upper())
server.close()
