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


def auth(auth_type):
  print('auth_func:', auth_type)

  def outer_wrapper(func):
    def wrapper(*args, **kwargs):
      print('wrapper func args', args)
      if auth_type == 'local':
        username = input('Username:').strip()
        password = input('Password:').strip()
        if user == username and passwd == password:
          print('\033[32; ImUser has passes anthentication\033[0m')
          res = func(*args, **kwargs)
          print('---after authentication')
          return res
        else:
          exit('\033[31; ImInvalid username or password\033[0m')
      elif auth_type == 'ladp':
        print('搞毛线ladap, 不会....')

    return wrapper

  return outer_wrapper


def index():
  print('welcome to index page')


# 本地认证
@auth(auth_type='local')  # home = wrapper()
def home():
  print('welcome to home page')
  return 'from home'


# 远程认证
@auth(auth_type='ladp')
def bbs():
  print('welcome to bbs page')


index()
home()
bbs()
