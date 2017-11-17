import time

# 高阶函数
# 函数即 "变量"
'''
  a: 把一个函数名当做实参传给另外一个函数
  b: 返回值中包含函数名
'''


def test(a):
  print(123)
  while a > 0:
    print(a)
    break


test(1)


def bar():
  time.sleep(3)
  print('in the bar')


# 统计 bar 函数运行时间
# bar 相当于内存地址  门牌号 映射的地址
def test1(func):
  # print(func)
  start_time = time.time()
  func()  # 可以运行 运行bar这个函数
  stop_time = time.time()
  print('the func run time %s' % (stop_time - start_time))


test1(bar)
