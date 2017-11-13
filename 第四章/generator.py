import time

L = [x * x for x in range(10)]
print(L)
# generator
g = (x * x for x in range(10))
print(g)


# 打印出来
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for n in g:
#  print(n)


def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print(b)
    a, b = b, a + b
    n = n + 1
  return 'done'


# fib(10)


# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行.
def fibs(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n += 1
  return 'done'


x = fibs(10)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print('aaaa')
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
for xs in x:
  print(xs)

k = fibs(10)
while True:
  try:
    x = next(g)
    print('g:', x)
  except StopIteration as e:
    print('Generator return value', e.value)
    break


# demo

def consumer(name):
  print('%s 准备吃包子!' % name)
  while True:
    baozi = yield
    print('包子[%s]来了!,被[%s]吃了!' % (baozi, name))


def producer(name):
  c = consumer('A')
  c2 = consumer('B')
  c.__next__()
  c2.__next__()
  print('%s准备开始做包子啦!' % name)
  for i in range(10):
    time.sleep(1)
    print('做了两个包子了!')
    c.send(i)
    c2.send(i)


# producer('alex')

"""
迭代器
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：
"""
from collections import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print((x for x in range(10)))

'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''

for x in [1, 2, 3, 4, 5]:
  pass

it = iter([1, 2, 3, 4, 5])
while True:
  try:
    x = next(it)
  except StopIteration:
    break

# demo
user_status = False


def login(func):
  _username = 'alex'
  _password = 'abc123'
  global user_status

  if user_status == False:
    username = input('user:')
    password = input('password:')
    if username == _username and password == _password:
      print('welcome login...')
      user_status = True
    else:
      print('wrong username or password!')
  else:
    print('用户已登录,验证通过...')

  if user_status == True:
    func()


def home():
  print('----首页----')


def america():
  # login()
  print('----欧美专区----')


def japan():
  print('----日韩专区----')


def henan():
  # login()
  print('----河南专区----')


home()
login(america)
login(henan)

'''
封闭：已实现的功能代码块不应该被修改
开放：对现有功能的扩展开放
'''

user_statuss = False


def loginn(auth_type):
  def auth(func):
    def inner(*args, **kwargs):
      if auth_type == 'qq':
        _username = 'alex'
        _password = '123abc'
        global user_statuss

        if user_status == False:
          username = input('user:')
          password = input('password:')

          if username == _username and password == _password:
            print('welcome login...')
            user_statuss = True
          else:
            print('wrong username or password!')

        if user_statuss == True:
          return func(*args, **kwargs)
      else:
        print('only support qq')

    return inner

  return auth


def home():
  print('首页')


@loginn('qq')
def americaa():
  print('欧美')


@loginn('weibo')
def henans(style):
  '''
    :param style: 喜欢看什么类型的，就传进来
    :return:
  '''
  print('----河南专区---')


america()
henans()
