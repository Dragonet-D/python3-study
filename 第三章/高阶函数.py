# 变量可以指向函数，函数的参数能够接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(m, n, abs):
  return abs(m - n)


print(add(1, 11, abs))
