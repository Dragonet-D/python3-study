import time, datetime, random

# print(time.clock())
print(time.altzone)
print(time.asctime())
print(time.localtime())
print(time.gmtime(time.time() - 800000))

print(datetime.datetime.now())
print(datetime.date.fromtimestamp(time.time()))
print(datetime.datetime.now() + datetime.timedelta(3))
print(datetime.datetime.now() + datetime.timedelta(minutes=30))

c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))

print(datetime.datetime.now())

# 随机数
print(random.random())
print(random.randint(1, 2))
print(random.randrange(1, 20))

checkcode = ''
for i in range(4):
  current = random.randrange(0, 4)
  if current != i:
    temp = chr(random.randint(65, 90))
  else:
    temp = random.randint(0, 8)
  checkcode += str(temp)
print(checkcode)
