# 在一个函数的函数体内用def去声明而不是去调用

def foo():
  print('in the foo')

  def bar():
    print('in the bar')

  bar()


foo()

# bar() # 局部变量存在于函数当中;


# 函数的调用
# def test1():
#  test2()

# test1()

# 作用域 只能从内往外找
x = 0


def grandpa():
  def dad():
    x = 2
    print('dad %s' % x)

    def son():
      x = 3
      print('son %s' % x)

    son()

  dad()
  print('grandpa %s' % x)


grandpa()
