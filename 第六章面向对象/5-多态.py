# 同一个接口, 多种实现
class Animal(object):
  def __init__(self, name):
    self.name = name

  @staticmethod
  def animal_talk(obj):
    obj.talk()

  def talk(self):
    pass


class Cat(Animal):
  def talk(self):
    print('Meow')


class Dog(Animal):
  def talk(self):
    print('Woof! Woof!')


d = Dog('陈荣华')
# d.talk()
c = Cat('徐亮为')
# c.talk()
Animal.animal_talk(c)
Animal.animal_talk(d)
