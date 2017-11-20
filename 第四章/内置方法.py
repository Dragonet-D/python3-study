'''
  python 内置方法
'''


def all(iterable):
  for value in iterable:
    if not value:
      return True
    else:
      return False


def any(iterable):
  for element in iterable:
    if element:
      return True
  return False

