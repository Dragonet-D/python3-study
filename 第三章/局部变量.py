# def changename(name):
#   print('before change')
#   # 局部变量 局部作用域 只能在这个函数里面生效
#   name = 'Alex'
#   print('after change')
#   # print(name)
#   return getName(name)
#
#
# def getName(name):
#   print(name)
#   return name
#
#
# """
#   局部变量
# """
#
# name = 'alex'
# changename(name)
# print(name)
# print(changename(name))
#
# # 改全局变量
# school = 'Old Boy'
#
#
# def change_name():
#   # 全局声明
#   global school
#   school = 'Mage Linux'
#   print(school)
#
#
# change_name()

'''
  不要用global
'''


def chang_name():
  global name
  name = 'alex'


chang_name()
print(name)

names = ['alex', 'jack', 'rain']


# 元祖
# touples = (1, 2, 3, 4)


def chang_list(names):
  names[0] = 'hello'
  print(names)


print(names)
chang_list(names)

'''
  在子程序中定义的变量就是局部变量,
  当局部变量与全局变量重名的时候,局部变量生效
'''