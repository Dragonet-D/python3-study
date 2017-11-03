import sys
# 自动关闭文件
# with open('yesterday', 'r', encoding='utf-8') as f, \
#     open('yesterday.bat', 'r', encoding='utf-8') as f2:
#   for line in f:
#     print(line)
# python 官方规范
# 一行代码 不应该操作80个字符
'''

'''
s = '你好'
s_to_gbk = s.encode('gbk')
print(s_to_gbk)
print(sys.getdefaultencoding())

