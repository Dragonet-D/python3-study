def test(x, y=1):
  print(x)
  print(y)


'''
  形式参数  形式存在 实际不存在
  位置参数  实参和形参一一对应的关系
'''

test(1, 3)


def test1(x, y):
  print(x)
  print(y)


x = 1
y = 12

# 关键字度调用与顺序无关
test(y=2, x=1)
test(x=y, y=x)

# 与形参一一对应
test(1, 3)

test(3, y=2)


def test2(x, y, z):
  print(x, y, z)


test2(1, 2, z=22)
