def changename(name):
  print('before change')
  # 局部变量 局部作用域 只能在这个函数里面生效
  name = 'Alex'
  print('after change')
  # print(name)
  return getName(name)


def getName(name):
  print(name)
  return name


"""
  局部变量
"""

name = 'alex'
changename(name)
print(name)
print(changename(name))

# 改全局变量
school = 'Old Boy'


def change_name():
  # 全局声明
  global school
  school = 'Mage Linux'
  print(school)


change_name()
