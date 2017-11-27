import mysql.connector # 导入MySQL驱动
conn = mysql.connector.connect(user='root', password='123456', database='test') # 注意把password设为你的root口令
cursor = conn.cursor()

# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))') # 创建user表
# cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'MinYaHui']) # 插入一行记录，注意MySQL的占位符是%s

cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)


conn.commit() # 提交事务
cursor.close()