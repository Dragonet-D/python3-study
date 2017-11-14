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


foo()


def bar():
  print('in the bar')
