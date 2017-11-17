import time


def test():
  time.sleep(3)
  print('in the test')


def timer(func):
  def deco(*args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    stop_time = time.time()
    print('the func runtime is %s' % (stop_time - start_time))

  # 返回内存地址
  return deco


@timer  # test1 = timer(test1)
def test1():
  time.sleep(3)
  print('in the test1')


@timer  # test2 = timer(test2)
def test2():
  time.sleep(3)
  print('in the test2')


@timer  # test3() = timer(test3) = deco  test3() = deco()
def test3(name):
  time.sleep(3)
  print('test3:', name)


# deco(test1)
# test1()  # test1() 执行的deco 后面执行的时候执行的是 func 参数 test1
test2()
test3('hello')
