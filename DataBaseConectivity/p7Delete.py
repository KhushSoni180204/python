import pymysql

eno = input("Enter Employee number = ")

connection = pymysql.connect(host="localhost",user="root",passwd="",database="database_python")

cursor = connection.cursor()

retrive = "DELETE FROM `emp1` where eno = '"+eno+"'"

print(retrive)

cursor.execute(retrive)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("Total records are",len(rows))

connection.commit()

connection.close()
