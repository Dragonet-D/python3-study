import pymysql
conn = pymysql.connect(host='192.168.0.102', port=3306, user='root', passwd='alex3714', db='testdb')
# 创建游标
cursor = conn.cursor()
effect_row = cursor.execute("select * from student")
print(effect_row)