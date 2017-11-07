"""
with open('a.txt', 'ab') as f:
  f.write('end action')
"""
import time


def logger():
  time_format = '%Y-%m-%d %X'
  time_current = time.strftime(time_format)
  with open('a.txt', 'a+') as f:
    f.write('%s end action\n' % time_current)


def test1():
  '''111'''
  print('test1 starting action...')
  logger()


def test2():
  '''111'''
  print('test2 starting action...')
  logger()


def test3():
  '''111'''
  print('test3 starting action...')
  logger()


test1()
test2()
test3()
