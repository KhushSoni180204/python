import pymysql
#database connection

connection = pymysql.connect(host="localhost",user="root",passwd="",database="database_python")

cursor = connection.cursor()

retrive = "select * from emp1;"

cursor.execute(retrive)

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()

connection.close()