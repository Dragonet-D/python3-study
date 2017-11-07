# 定义函数
def func1():
  """testing"""
  print('in the func1')
  return 0
func1()
print(func1())

# 定义过程 就是没有返回值的函数
def func2():
  '''testing1'''
  print('in the func2')

func2()
print(func2()) # None
x = func1()
y = func2()
print('from func1 return is %s' %x)
print('from func2 return is %s' %y) # None