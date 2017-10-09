print(abs(-12))
print(max(1,3))
print(type(int('123')))
print(type(float('12.34')))
print(type(str(123)))
print(type(bool(1)))
print(type(bool(0)))
print(bool(0))
a = abs
print(a(-123))

def myAbs(x):
  if x >= 0:
    return x
  else:
    return -x
def power(x):
  return x*x
print(power(123))

def powers (x,n):
  return x**n
print(powers(10,20))

def power1 (x,n):
  s = 1
  while n > 0:
    n = n -1
    s = s*x
  return s
print(power1(5,3))

def power2(x,n = 2):
  s = 1
  while n>0:
    n = n-1
    s=s*x
  return s
print(power2(5))
print(power2(5,2))

def enroll(name,gender):
  print("name:",name)
  print("gender:",gender)
print(enroll('jay','male'))

def enroll1(name,gender,age=6,city='Beijing'):
  print("name:",name)
  print("gender:",gender)
  print("age:",age)
  print("city:",city)
enroll1('Tom','Famale')

def addEnd(L=None):
  if L is None:
    L = []
  L.append('END')
  return L
print(addEnd())
print(addEnd())

def addEnd1(L=[]):
  L.append('END')
  return L
print(addEnd1())
print(addEnd1())

def calc(numbers):
  sum = 0
  for n in numbers:
    sum = sum + n*n
  return sum
print(calc([1,2,3,4]))

def calc1(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n*n
  return sum
print(calc1(1,2,3,4))

nums = [1,2,3]
print(calc1(nums[0],nums[1],nums[2]))
print(calc1(*nums))

#关键字参数
def person(name,age,**kw):
  print("name:",name,"age:",age,"other:",kw)
person("Micheal",30)
person('Tom',12,city="Beijjing",gender="M",job="Engineer")
extra = {
  'city':'Beijing',
  'job':'Engineer'
}
person('Tom',12,**extra)

def person1(name,age,**kw):
  if 'city' in kw:
    pass
  if 'job' in kw:
    pass
  print("name:",name,"age:",age,"other:",kw)
person1("Jack",24,city='Beijing',addr="Chaoyang",zipcode=123456)

def person2(name,age,*,city,job):
  print(name,age,city,job)
person2('Jack',24,city="Beijing",job="Engineer")

def person3(name,age,*args,city,job):
  print(name,age,args,city,job)
person3('jay',24,'div','meta',city='Beijing',job='python')

def person4(name,age,*,city="BeiJing",job):
  print(name,age,city,job)
person4('Jay',23,job='Engineer')
#参数组合
