#dict
names = ['aa','aaa','vvvv']
scores = [95,75,85]
d = {
  'Michael':95,
  'Bob':75,
  'Tracy':85,
  'Alice':90
}
print(d['Michael'])
#判断key是否存在
print('Michael' in d)
print('Tom' in d)
print(d.get('Michael'))
print(d.get('Tom'))
d.pop('Alice')
print(d)

#set
s = set([1,2,3])
print(s)
a = set([1,2,3,1,3,1,2])
print(a)
a.add(4)
print(a)
a.add(5)
print(a)
a.remove(2)
print(a)
b = ['v','a','f']
b.sort()
print(b)

c = 'abc'
d = c.replace('a','A')
print(c)
print(d)
e = set([1,2,3,4,51,13,1,2,3])
print(e)