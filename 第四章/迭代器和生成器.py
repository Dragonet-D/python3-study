# 列表生成式
'''
  将临时变量i存到i再*2
'''
x = [i * 2 for i in range(10)]
print(x)

a = []
for i in range(10):
  a.append(i * 2)
print(a)


def func(i):
  print(i)


y = [func(i) for i in range(10)]

# 通过列表生成式,我们可以创建一个列表;但是收到内存的限制;而且包含一个一百万元素的列表,不仅占用很大的储存空间.如果我们只要一小部分就浪费空间

print(range(10))

# 生成器
t = (i * 2 for i in range(100000000))
yy = (i * i for i in range(10))
# <generator object <genexpr> at 0x007491E0>
# 能够立刻返回 列表准备好了 只会循环到那里才能获取到
# 生成器不能用切片去取
# 生成器只有在调用的时候才会生成相应的数据
# 生成器有一个next 方法
# 没有一个方法让你回到前一个
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())


# 生成一个[1,3,5] 的列表
# 只有一个方法 一直 __next()__ 一直向下取
# 只记录当前的位置
# 只有一个__next__()方法
# for i in t:
#  print(i)

# 斐波那契数列
# def fib(max):
#   n, a, b = 0, 0, 1
#   while n < max:
#     print(b)
#     a, b = b, a + b
#     n += 1
# fib(10)


# generator 函数做的生成器
def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n += 1
  return 'done'  # 用for循环就不会打印 是异常的时候打印的消息


# 变成了生成器
print(fib(10))  # <generator object fib at 0x02169480>
f = fib(10)

while True:
  try:
    x = next(f)
  except StopIteration as e:
    print(e.value)
    break

print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

# 还可通过 yield 实现在单线程的情况下实现并发运算的效果

