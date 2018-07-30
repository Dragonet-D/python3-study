import pymysql
conn = pymysql.connect(host='192.168.0.102', port=3306, user='root', passwd='alex3714', db='testdb')
# 创建游标
cursor = conn.cursor()
effect_row = cursor.execute("select * from student")
# print(cursor.fetchone())

data = [
    (5, "xiaolong", "2015-02-12"),
    (15, "xiaoming", "2015-03-12"),
    (25, "xiaofeng", "2015-04-12"),
]
cursor.executemany("insert into student (age, name, register_date) values (%s, %s,%s)", data)
conn.commit()
conn.close()
