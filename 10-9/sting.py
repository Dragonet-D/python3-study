name = 'my name is {name} and i am {year} old'
# 两个下划线的是内部的方法
# 首字母大写
print(name.capitalize())
# 统计a出现的次数
print(name.count('a'))
# 一共打印50个  不够的就用'-'补上 放在中间
# -----------------my name is alex------------------
print(name.center(50, '-'))
# 转成二进制
print(name.encode())
# 判断以什么结尾
print(name.endswith('a'))
# 把tab键转换成多少个空格
print(name.expandtabs())
# 查找 返回下标
print(name[name.find('name'):])
# 找不到就返回 -1
print(name.find('b'))

print(name.format(name='alex', year=23))
print(name.format_map({'name': 'alex', 'year': 12}))
# 阿拉伯数字加阿拉伯字符
print('ab123'.isalnum())  # true
print('ab123!'.isalnum())  # false
# 纯英文字符
print(name.isalpha())  # false
# 16 进制
print('1'.isdecimal())
# 整数
print('1'.isdigit())  # true
print('name'.isidentifier())  # 判断是不是一个合法的标识符 合法的变量名
# 转小写
print(name.lower())
print(name.upper())
# 是不是数字
print('22'.isnumeric())
print('33A'.isspace())  # 是不是个空格
print(' '.isspace())
# 首字母大写
print('My Name Is'.istitle())
# 是不是能够打印的
print('My Name Is'.isprintable())  # tty file, drivefile
print(name.isupper())
print(name.join('=='))
# 列表变成字符串
print('=='.join(['1', '2', '3', '4']))
# 长50 不够用*
print(name.ljust(50, '*'))
print(name.rjust(50, '*'))
print('ALEX'.lower())
print('alex'.upper())
# 去掉左边的空格和回车
print(' Alex\n'.lstrip())
print('  Alex\n'.rstrip())
print('   Alex\n'.strip())
print('-----------')

# 把对应的字符串转换为后面的值
p = str.maketrans('abcdef', '123456')
print('alex li'.translate(p))

print('alex li'.replace('l', 'L', 1))
# 返回从左往右 找到最右边的值的下标
print('alex li'.rfind('l'))
# 字符串变成列表
print(name.split(' '))
print('1+2+3+4'.split('+'))
# 按照换行分
print('1+2+\n+d'.splitlines())
print(name.startswith('a'))
# 转大写
print(name.swapcase())
# 转换为title
print(name.title())
# 不够的用0填充
print('lex li'.zfill(50))
# 对字符串的修改相当于生成一个新的字符串
