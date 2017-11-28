# 属性方法 感觉像计算属性  不能传参  但是可以返回结果
# 属性方法对于用户来说不用关心实现方法, 只需要得到这个状态
class Person(object):
  def __init__(self, name):
    self.name = name
    self.__food = None

  @property
  def eat(self):
    print('%s eat %s' % (self.name, self.__food))

  @eat.setter
  def eat(self, food):
    print('set to food:', food)
    self.__food = food


p = Person('柯基犬')
p.eat
p.eat = '包子'
p.eat
# 把一个方法变成一个静态属性
