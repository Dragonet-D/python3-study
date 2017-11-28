def bark(self):
  print('%s is barking' % self.name)


class Dog(object):
  def __init__(self, name):
    self.name = name

  def eat(self, obj):
    print('%s is eating %s' % (self.name, obj))


d = Dog('牛汉阳')
choice = input('>>:').strip()
# 判断是不是有某个属性或者方法
# print(hasattr(d, choice))

# print(getattr(d, choice))
if hasattr(d, choice):
  func = getattr(d, choice)
  func('chenronghua')
else:
  # setattr(d, choice, bark)
  # d.talk(d)
  # 设置属性
  setattr(d, choice, 22)
  print(getattr(d, choice))
'''
  反射 
    hasattr(obj,name), 判断一个对象obj里是否有对应name的字符串的方法
    getattr(obj,name), 根据字符串去获取obj对象里的对应的方法的内存地址
    setattr(obj,name,value) 设置obj的name 为value
    delattr(obj,name) 删除obj的name 属性
'''
