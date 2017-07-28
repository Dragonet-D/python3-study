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