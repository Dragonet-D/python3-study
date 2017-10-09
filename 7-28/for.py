'''
age_of_oldboy = 56
for i in range(3):
  guess_age = int(input("guess age:"))
  if guess_age == age_of_oldboy:
    print("yes you got it")
    break
  elif guess_age > age_of_oldboy:
    print('123')
  else:
    print('234')
else:
  print('you have tried too many times')
'''

#for i in range(0,10,2):
# print("loop:",i)
'''
for i in range(0,10):
  if i < 5:
    print("loop:",i)
  else:
    continue
  print('呵呵。。。')
'''
for i in range(10):
  print('---------',i)
  for j in range(10):
    print(j)
    if j > 5:
      break

names = ['aa','bb']
for name in names:
  print(name)

for x in [1,2,3,4,5,6]:
  print(x)

sum = 0
for x in range(101):
  sum += x
print(sum)

print(range(10))

sum1 = 0
n = 99
while n > 0:
  sum1 = sum1 + n
  n = n - 2
print(sum1)
L = ['Bart','Lisa','Adam']
for name in L:
  print('Hello',name)
