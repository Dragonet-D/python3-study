class AlexException(Exception):
  def __init__(self, msg):
    self.message = msg

  def __str__(self):
    '''打印的时候返回的格式'''
    return self.message


try:
  '''触发自己写的异常  raise '''
  raise AlexException('数据库连不上')
except AlexException as e:
  print(e)
