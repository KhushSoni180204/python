import pymysql

dname = input("Enter Employee Department name = ")

connection = pymysql.connect(host="localhost",user="root",passwd="",database="database_python")

cursor = connection.cursor()

retrive = "select * from emp1 where dname='"+dname+"'"

print(retrive)

cursor.execute(retrive)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("Total records are",len(rows))

connection.commit()

connection.close()
