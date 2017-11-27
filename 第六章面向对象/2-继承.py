# class People: 经典类
class People(object):  # 新式类
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def eat(self):
    print('%s is eating' % self.name)

  def sleep(self):
    print('%s is sleeping' % self.name)

  def talk(self):
    print('%s is talking' % self.name)


class Relation(object):
  def make_friends(self, obj):
    print('%s is making friends with %s' % (self.name, obj.name))


class Man(People, Relation):
  def __init__(self, name, age, money):
    # People.__init__(self, name, age) # 经典类的写法
    # 另一种写法
    super(Man, self).__init__(name, age)  # 新式类的写法
    self.money = money
    print('%s 一出生就有 %s money' % (self.name, self.money))

  def piao(self):
    print('%s is piaoing.......20s....is ending' % self.name)

  def sleep(self):
    # 扩展父类方法
    People.sleep(self)  # 把 m1 传进去
    print('man is sleeping')


class Woman(People, Relation):
  def getBirth(self):
    print('%s is born a baby' % self.name)


m1 = Man('NiuHanYang', 22, 10)
# m1.eat()
# m1.sleep()
# m1.piao()
# print(m1.money)

w1 = Woman('ChenRongHua', 26)
w1.getBirth()

m1.make_friends(w1)
