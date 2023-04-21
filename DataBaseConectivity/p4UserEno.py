import pymysql

eno1 = input("Enter eno from = ")

eno2 = input("Enter eno to = ")

connection = pymysql.connect(host="localhost",user="root",passwd="",database="database_python")

cursor = connection.cursor()

retrive = "select * from emp1 where eno between '"+eno1+"' and '"+eno2+"'"

print(retrive)

cursor.execute(retrive)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("Total records are",len(rows))

connection.commit()

connection.close()
