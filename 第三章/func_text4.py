def test1():
  """函数描述"""
  print('in the test1')
  return 0

test1()
x = test1()
print('%s aaaa' %x)

def test2():
  """函数描述"""
  print('in the test2')
  return 1

def test3():
  """函数描述"""
  print('in the test3')
  return 1, 'hello', ['alex','wupeiqi'], {'name': 'alex'}
x = test1()
z = test3()
print(z)
print(type(z))
y = test2()
print(type(y))
print(type(x))
"""
  返回值数=0; 返回None
  返回值数=1; 返回object
  返回值数>1; 返回tuple
"""