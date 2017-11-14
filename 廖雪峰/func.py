# -*- coding: utf-8 -*-
print(float('12.34'))
print(str(1.23))
print(bool(1))
print(bool(0))
print(bool(''))
a = abs
print(a(-1))


def my_abs(x):
  if x > 0:
    return x
  else:
    return -x


def power(x, n):
  s = 1
  while n > 0:
    n = n - 1
    s = s * x
  return s


print(power(5, 3))


def add_end(L=None):
  if L is None:
    L = []
  L.append('end')
  return L


print(add_end())


def calc(numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum


print(calc([1, 2, 3, 4]))


def calcs(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum


print(calcs(1, 2, 3, 4, 5, 6))


def person(name, age, **kw):
  print(name, age, kw)


person('nihao', 123, sex='f', gender='Engineer')


def person1(name, age, **kw):
  if 'city' in kw:
    pass
  if 'job' in kw:
    pass
  print(name, age, kw)


person1('jack', 24, city='beijing', addr='chaoyang', zipcode=123456)

