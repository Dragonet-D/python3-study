import time


def timer(func):
  def deco():
    start_time = time.time()
    func()
    stop_time = time.time()
    print('the func runtime is %s' % (stop_time - start_time))

  return deco


@timer
def test():
  time.sleep(3)
  print('in the test')
