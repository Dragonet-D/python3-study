# data = open("yesterday",encoding="utf-8").read()
# f = open("yesterday",'w',encoding="utf-8")
# r 读
# w 写 是创建一个文件;会覆盖前面的内容
# 文件句柄 文件的内存对象
# print(data)
# data = f.read()
# data2 = f.read()
# print(data)
# 文件是一行一行的  文件一行一行的读完了  执行文件句柄的时候 从后面接着开始读 相当于从光标的位置开始读 读完一遍就没了;如果想读出内容就把光标移回去
# print('------------data2---------%s--' %data2) # 空的
# f.write("我爱北京天安门,天安门上太阳升\n")
# f.write("天安门上太阳升")


# f = open("yesterday", 'a', encoding="utf-8")
# # a 是append的意思 追加
# f.write('\n我爱北京天安门.......')
# data = f.write('123')
# print('---read', data)
# # 不可 读
# f.close()

f = open('yesterdays','a', encoding="utf-8") # 文件句柄
# for i in range(5):
#   print(f.readline())
# print(f.readlines())

#low loop
'''
for index,line in enumerate(f.readlines()):
  if(index == 9):
    print('-----我是分割线-----')
    continue
  print(line.strip())
'''

# high bige
# 一行一行的读 读完释放内存
'''
count = 0
for line in f:
  if count == 9:
    print('--------------')
    count += 1
    continue
  print(line)
  count += 1
'''

# 打印焦点的位置
# 按照字符计数
# print(f.tell())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.tell())
# # 光标回到某个地方
# f.seek(10)
# print(f.readline().strip())
# print(f.tell())
# # 编码
# print(f.encoding)
# #
# print(f.buffer)
# # errors
# print(f.errors)
# # fileno 返回一个文件句柄在类里面的编号
# print(f.fileno())
# # name
# print(f.name)
# # seekable 如果是字符串是可以移的;
# print(f.seekable())
# # readable 判断文件是否可读
# print(f.readable())
# # writeable
# print(f.writable())
# # flush 默认等到缓存满了再写到内存里面
# # 强制刷新 写一行刷一行 刷到内存中
# print(f.flush())
# print(f.closed)
#
# print(f.closed)
# # truncate 截断
# # 什么都不写就清空
# # f.seek(10)
# f.truncate(20)
#
# # 读写
# ff = open('yesterday','r+',encoding='utf-8')
# print(ff.readline())
# print(ff.readline())
# print(ff.readline())
# print(ff.tell())
# # 以读和追加的形式打开
# ff.write('-------------diao----------') # 追加到最后
# print(ff.readline())
# # 写读 先创建文件 再往里面写
# fff = open('yesterdayss','w+',encoding='utf-8')
# fff.write('----------dio--------------\n')
# fff.write('----------dio--------------\n')
# fff.write('----------dio--------------\n')
# fff.write('----------dio--------------\n')
# fff.write('----------dio--------------\n')
# print(fff.tell())
# fff.seek(10)
# print(fff.tell())
# print(fff.readline())
# fff.write('should ba at the begining of the second line')
# # 只能追加最后
# # 硬盘的存储机制
# # 不能插入 如果插入会覆盖后面的东西
# # 在源文件上的修改 会直接把内容覆盖
#
# # 追加读写
# ffff = open('yesterdayss','a+',encoding='utf-8')
#
# # 读 二进制文件
# aa = open('yesterdays','rb')
# # 什么情况下用 rb 网络传输只能用二进制
# print(aa.readline())
# print(aa.readline()) #  binary mode doesn't take an encoding argument
# print(aa.readline())
#
# fff.close()
#
#
# f.close()

# 写 二进制文件 文件是以二进制编码处理 我们看大的就是字符串
f = open('yesterdays', 'wb') #
f.write('hello binary\n'.encode()) # 转成二进制 不写默认utf-8
f.close()