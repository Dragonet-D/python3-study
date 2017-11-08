def test(x, y, z=12):
  print(x)
  print(y)


test(1, 2)
# 关键字调用
test(x=1, y=12, z=123)


# 实参不固定 参数组
def test1(*args):
  print(args)


test1(1, 2, 3, 4, 5, 65, 6)
test1(*[1, 2, 3, 4, 5])  # args = tuple([1,2,3,4,5])
print([*[1, 2, 3, 4, 5, 6]])


# *args 接收N个位置 参数转换成元祖的方式
def test2(x, *args):
  print(x)
  print(args)


test2(1, 2, 3, 4, 5)


# 传字典
# **kwargs: 把n个关键字参数 转换成字典的方式
def test3(**kwargs):
  print(kwargs)
  print(kwargs['name'])
  print(kwargs['age'])
  print(kwargs['sex'])


# 关键字参数
test3(name='alex', age=8, sex='F')


# test3(**{'name':'alex','age':8})

# print(*[1,2,3,45])

def test4(name, **kwargs):
  print(name)
  print(kwargs)


test4('alex')
test4('alex', names='hello')


def test5(name, age=18, **kwargs):
  print(name)
  print(age)
  print(kwargs)


test5('a', age=1233, naaa='123', hobby='tesla')
test5('a', 1233, naaa='123', hobby='tesla')
test5('a', naaa='123', hobby='tesla')
test5('a', naaa='123', hobby='tesla', age=22)


def test6(name, age=18, *args, **kwargs):
  print(name)
  print(age)
  print(args)
  print(kwargs)
  logger('test4')


def logger(source):
  print('from %s' % source)


test6('alex', 34, sex='m', hobby='tesla')


# test6('alex', 34, 12, 123, sex='m', hobby='tesla')

def func_name(arg1, arg2, arg3, *args, **kwargs):
  pass


func_name(5, 3)
'''
  位置参数
'''
