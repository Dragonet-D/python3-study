import time

# def timer(func):
#   def deco(*args, **kwargs):
#     start_time = time.time()
#     func(*args, **kwargs)
#     stop_time = time.time()
#     print('the func runtime is %s' % (stop_time - start_time))
#
#   return deco
#
#
# @timer
# def test():
#   time.sleep(3)
#   print('in the test')
user, passwd = 'alex', 'abc123'


def auth(func):
  def wrapper(*args, **kwargs):
    username = input('Username:').strip()
    password = input('Password:').strip()
    if user == username and passwd == password:
      print('\033[32; ImUser has passes anthentication\033[0m')
      res = func(*args, **kwargs)
      print('---after authentication')
      return res
    else:
      exit('\033[31; ImInvalid username or password\033[0m')

  return wrapper


def index():
  print('welcome to index page')


@auth
def home():
  print('welcome to home page')
  return 'from home'


@auth
def bbs():
  print('welcome to bbs page')


index()
print(home())
