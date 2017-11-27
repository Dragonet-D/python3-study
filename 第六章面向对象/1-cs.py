'''
  面向对象的三大特性:
    封装, 继承, 多态
'''


class Role(object):
  n = 123  # 类变量
  name = '我是类name'

  def __init__(self, name, life, gun_name):
    '''构造函数'''
    # 在实例化时做一些类的初始化的工作
    self.name = name  # 实例变量(静态属性), 实例变量的作用域就是实例本身
    self.life = life
    self.gunName = gun_name

  def __del__(self):
    '''析构函数'''
    print('%s 彻底死了' % self.name)

  def shot(self, gun_name):  # 类的功能,方法(动态属性)
    print('gun_name is %s' % gun_name)


'''
  实例变量和类变量
    实例变量的作用域就是实例本身
    先找实例本身,找不到就找类里面
    
    类变量的用途? 大家公用的属性
    (大家公共的属性都是一样的, 如果有14亿人, 每个都是中国, 如果用默认参数就会生成14亿个实例, 节约内存)
'''


class Person:
  cn = '中国'

  def __init__(self, name, age, addr):
    self.name = name
    self.age = age
    self.addr = addr


p1 = Person('a', 12, '11')

'''
  把一个类变成一个具体对象的过程叫做实例化
'''
# 实例化
#  Role(r1,'Alex','AK47')
'''
  r1.name = 'Alex'
  r1.gun = 'AK47'
'''
# 类变量
print(Role.n)  # 123
print(Role.name)  # 我是类name
# 生成一个对象这个对象就是Role的实例
r1 = Role('alex', 100, 'AK47')  # 实例化生成一个角色
# del r1 # 销毁
print(r1.n)  # 123
print(r1.name)  # alex
r1.shot('AK47')  # Role().shot(r1)

'''
  析构函数: 
    在实例释放, 销毁的时候自动执行的,通常用于一些收尾工作,通常用于一些打开一些临时文件,数据库链接
'''

'''
  私有方法,属性
'''


class Demo:
  def __init__(self, name, age, life_value=100):
    '''构造函数'''
    self.name = name
    self.age = age
    # 私有属性 __  外面访问不了 内部可以改
    self.__life_value = life_value

  # 私有方法
  def __personal(self):
    print('这是个私有方法')

  def show_status(self):
    print('life value is %s' % self.__life_value)

  def gun(self, gun_name):
    print('gun is %s' % gun_name)


d1 = Demo('AK47', 12)
d1.gun('AK47')  # Demo().gun(d1)
d1.show_status()
