import sys

# 自动关闭文件
# with open('yesterday', 'r', encoding='utf-8') as f, \
#     open('yesterday.bat', 'r', encoding='utf-8') as f2:
#   for line in f:
#     print(line)
# python 官方规范
# 一行代码 不应该操作80个字符
'''
  3.0 默认unicode
  utf-8 是unicode的扩展
  unicode支持中文 全以两个字节存
  unicode是utf-8和gbk 的翻译
'''
s = '你好'
s_to_gbk = s.encode('gbk')
print(s_to_gbk)
print(sys.getdefaultencoding())

a = '我是中国人'.encode('utf-8')
print(a)