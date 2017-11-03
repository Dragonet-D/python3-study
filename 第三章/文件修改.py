# 文件修改
# 1 打开文件把文件内容加到内存里
# 2 打开一个文件 修改完了 放到另一个文件里
# import sys

f = open('yesterday', 'r', encoding='utf-8')
f_new = open('yesterday.bat', 'w', encoding='utf-8')

# find_str = sys.argv[1]
# replace_str = sys.argv[2]
#
# for line in f:
#   if find_str in line:
#     line = line.replace(find_str, replace_str)
#   f_new.write(line)

for line in f:
  if '肆意的快乐等着我' in line:
    line = line.replace('肆意的快乐等着我', '肆意的快乐等着Alex')
  f_new.write(line)

f.close()
f_new.close()
