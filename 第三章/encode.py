#-*-coding:gbk-*-
'''
  ����֮�以��ת����Ҫͨ�� unicode  ��decode()��unicode  ����unicode֮ǰ��ʲô�����ʽ  ��encode()����Ҫת���ĸ�ʽ
'''
import sys
print(sys.getdefaultencoding())
s = '���'
print(s.encode('gbk'))
print(s.encode('utf-8'))
print(s.encode('utf-8').decode('utf-8').encode('gb2312'))
print(s.encode('utf-8').decode('utf-8').encode('gb2312').decode('gb2312'))
