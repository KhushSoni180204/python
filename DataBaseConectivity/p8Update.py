import pymysql

eno = input("Enter Employee number = ")
ename = input("Enter Employee name = ")
salary = input("Enter Employee Salary = ")
dname = input("Enter Department name = ")
eno1 = input("Enter Employee number to update = ")
connection = pymysql.connect(host="localhost",user="root",passwd="",database="database_python")

cursor = connection.cursor()

retrive = "UPDATE `emp1` SET `eno`='"+eno+"',`ename`='"+ename+"',`salary`='"+salary+"',`dname`='"+dname+"' WHERE eno = '"+eno1+"'"

print(retrive)

cursor.execute(retrive)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("Total records are",len(rows))

connection.commit()
connection.close()