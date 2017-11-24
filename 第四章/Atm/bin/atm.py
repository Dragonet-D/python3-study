import os
import sys

'''
  想导入 core 文件夹下面的main
  环境变量
'''
# print(__file__)
# 绝对路径
# print(os.path.abspath(__file__))
# 相对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# import conf, core
from conf import settings
from core import main

main.login()
