class Dog(object):
  def __init__(self, name):
    self.name = name

  def eat(self):
    print('a dog is eating')


d = Dog('柯基犬')
choise = input('>>:').strip()
# 异常处理
try:
  getattr(d, choise)
except AttributeError as e:
  print('没有这个属性', e)

names = ['alex', 'jack']
# names[3]
data = {
  'name': '1123'
}
# data['name']

# try:
#   names[3]
#   data['name']
# except (KeyError, IndexError) as e:
#   print('没有这个key', e)
# except IndexError as e:
#   print('列表操作错误', e)


'''
  这样写不能判断具体的错, 两种错都用同样的方法来处理的话就这样写
'''
try:
  names[1]
  data['name']
except (KeyError, IndexError) as e:
  print('没有这个key', e)
except Exception as e:  # 抓所有未知的错误
  print(e)
else:
  print('一切正常')
finally:
  print('不管有错没错都执行')
'''
  抓住所有的错误
'''
try:
  # names[3]
  open('test.txt')
except Exception as e:
  print('出错了', e)

'''
  异常: 
    try:
      code
    except (Erro1,Erro2) as e:
      print(e)
'''
s1 = 'hello'
try:
  int(s1)
except ValueError as e:
  print(e)
