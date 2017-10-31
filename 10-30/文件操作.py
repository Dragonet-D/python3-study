# data = open("yesterday",encoding="utf-8").read()
# f = open("yesterday",'w',encoding="utf-8")
# r 写
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

f = open('yesterdays', encoding="utf-8") # 文件句柄
# for i in range(5):
#   print(f.readline())
# print(f.readlines())
for index,line in enumerate(f.readlines()):
  print(line.strip())