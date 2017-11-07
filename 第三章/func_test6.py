def test(x, y=2):
  print(x)
  print(y)


test(1, 13)

# 默认参数的特点:
'''
  调用函数的时候 默认参数非必传
'''
# 默认参数用途
'''
  用途: 1\ 默认安装值
  2\ 链接数据库的端口号 
'''
def conn(host, port=3306):
  pass
conn()