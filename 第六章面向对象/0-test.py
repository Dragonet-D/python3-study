class Person(object):
  def __init__(self, name):
    self.name = name

  def get_name(self):
    print('this name is %s' % self.name)


p1 = Person('Alex')
p1.get_name()
