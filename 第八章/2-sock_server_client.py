import socket

client = socket.socket()
client.connect(('localhost', 9999))

while True:
  cmd = input('>>:').strip()
  if len(cmd) == 0: continue
  client.send(cmd)
  cmd_res = client.recv(1024)

  print(cmd_res)

client.close()
