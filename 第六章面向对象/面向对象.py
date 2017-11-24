def person(name, age, sex, job):
  data = {
    'name': name,
    'age': age,
    'sex': sex,
    'job': job
  }
  return data


def dog(name, dog_type):
  data = {
    'name': name,
    'type': dog_type
  }
  return data


d1 = dog('李磊', '京巴')
p1 = person('闫帅', 36, 'F', '前端')


def brak(d):
  print('dog %s:wang.wang.wang.wang.wang' % d['name'])


def walk(p):
  print('person %s is walking' % p['name'])


walk(p1)
brak(d1)
