import os


# os.system()
# 静态方法
class Dog(object):
  '''这个类是描述狗这个对象的'''

  def __init__(self, name):
    self.name = name

  @staticmethod  # 实际上跟类没什么关系了  把他和类的关联切断了, 变成了一个单纯的函数,非要说有什么关系是要在类下面调用
  def eat(self, food):
    print('%s is eating %s' % (self.name, food))


# 静态方法名义上归类管理,实际上不能调用任何类的属性和方法
d = Dog('陈荣华')
d.eat(d, '包子')
print(d.__doc__)


# 类方法
class Person(object):
  food = 'KFC'

  def __init__(self, name):
    self.name = name

  @classmethod
  def eat(self):
    print('haha %s' % self.food)
    # 类方法只能访问类变量, 不能访问实例变量


p = Person('kfc')
p.eat()
