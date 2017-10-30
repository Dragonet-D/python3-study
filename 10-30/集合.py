# 去重  关系测试 测试两个列表的 交集 并集
# 集合也是无序的

a = set([3, 4, 5, 6, 2, 3])
print(a)
list_1 = [1, 3, 4, 5, 234, 23, 2, 2, 3, 4, 5]
list_1 = set(list_1)
list_2 = set([2, 3, 45, 4, 6, 12, 34])
list_3 = set([1, 2, 4])
'''
print(list_1, type(list_1))  # <class 'set'>
print(list_1, list_2)
# 取交集 intersection & 
print(list_1.intersection(list_2))
print(list_1 & list_2)
# 并集 union
print(list_1.union(list_2))
# 差集 difference list_1里面有的 list_2里面没有的
# in list_1 but not in list_2
print(list_1.difference(list_2))
print(list_2.difference(list_1))
# 子集
print(list_1.issubset(list_2))  # False
print(list_3.issubset(list_1))  # True
# 父级
print(list_1.issuperset(list_2))  # False
print(list_1.issuperset(list_3))  # True
# 对称差集  去掉两个列表的交集
print(list_1.symmetric_difference(list_2))

print('--------------------------')
# 判断两个集合有没有交集
list_4 = set([5, 6, 8])
print(list_3.isdisjoint(list_4))  # True
'''
# 交集
print(list_1 & list_2)
# 并集
print(list_1 | list_2)
# 差集
print(list_1 - list_2) # in list_1 but not on list_2
# 对称差集
print(list_1 ^ list_2)
# subset and upperset 子集

# 操作
# 添加
list_1.add(1000)
list_1.update([1,2,3,4,56,7,664])
print(list_1)
# 删除
print(list_1.remove(5))
# pop 删除并返回当前的元素
# 长度
len(list_1)
# x in a
print(1 in list_1)
# x not in a
print(1 not in list_1)

