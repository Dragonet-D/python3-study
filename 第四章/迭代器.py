from collections import Iterable, Iterator

a = [1, 3, 4, 6, 7, 7, 8, 9, 11]
for index, i in enumerate(a):
  a[index] += 1
print(a)

aa = [i + 1 for i in range(10)]
print(aa)
# 迭代器 可直接作用于for循环的数据类型
# list tuple dict set str
# 一类是 generator 包括生成器和yield的generator function
# 可以使用isinstance 判断是不是iterable (可迭代的)
print(isinstance([], Iterable))

# 生成器不但可以作用域for循环,还可以被next()函数不断调用 并不断返回下一个值,知道最后抛出StopIteration错误标识无法继续返回下一个值了

# 可以被next()函数调用并不断返回下一个值的对象成为迭代器 Iteator

a = [1, 2, 3, 4]  # 是一个可迭代对象 但是不是一个迭代器 因为没有next()方法
print(dir(a))
# 生成器本身就是一个迭代器
print(isinstance((x for x in range(5)), Iterator))
print(isinstance((), Iterator))  # False

b = iter(a)
print(b.__next__())
print(b.__next__())
# list dict str 等数据类型不是Iterator
# 这是因为Python的Iterator对象标识一个数据流,Iterator对象可以被next()函数调用并不断返回下一个数据,知道没有数据时抛出StopIteration错误.可以把这个数据流看做是一个有序序列,但我们却不能提前知道序列的长度;只能不断通过next()函数实现按需计算下一个数据,所以Iterator的计算是惰性的.只有在需要返回下一个数据时他才会计算;
# Iterator 甚至可以表示一个无限大的数据流,例如全体自然数.而使用list是永远不可能储存全体自然数的;

'''
  能被for的就是Iterable的
  有next()方法的就是迭代器
'''

