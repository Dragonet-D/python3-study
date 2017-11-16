# def foo():
#   print('in the foo')
#   bar()
#
#
# foo()
# 出错 运行到bar的时候没定义

# def foo():
#   print('in the foo')
#   bar()
#
#
# def bar():
#   print('in the bar')
#
#
# foo()

def foo():
  print('in the foo')
  bar()


# foo()


def bar():
  print('in the bar')


class Studet(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def print_score(self):
    print('%s:%s' % (self.name, self.score))


bart = Studet('hahah', 59)
bart.print_score()