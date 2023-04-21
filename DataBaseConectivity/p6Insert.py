import pymysql

eno = input("Enter Employee number = ")

ename = input("Enter Employee name = ")

salary = input("Enter Employee Salary = ")

dname = input("Enter Department name = ")

connection = pymysql.connect(host="localhost",user="root",passwd="",database="database_python")

cursor = connection.cursor()

retrive = "INSERT INTO `emp1`(`eno`,`ename`,`salary`,`dname`) VALUES ('"+eno+"','"+ename+"','"+salary+"','"+dname+"')"

print(retrive)

cursor.execute(retrive)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("Total records are",len(rows))

connection.commit()

connection.close()
