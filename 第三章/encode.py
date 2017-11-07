#-*-coding:gbk-*-
'''
  编码之间互相转换都要通过 unicode  先decode()成unicode  告诉unicode之前是什么编码格式  再encode()成想要转换的格式
'''
import sys
print(sys.getdefaultencoding())
s = '你哈'
print(s.encode('gbk'))
print(s.encode('utf-8'))
print(s.encode('utf-8').decode('utf-8').encode('gb2312'))
print(s.encode('utf-8').decode('utf-8').encode('gb2312').decode('gb2312'))
