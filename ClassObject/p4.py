class Emp:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.branch = 0
        self.salary = 0
    def setdata(self):
        self.id = int(input("Enter employee id = "))
        self.name = input("Enter employee name = ")
        self.branch = int(input("Enter your branch 1,2,or,3 :"))
        if self.branch==1:
            self.salary=30000
        elif self.branch==2:
            self.salary=20000
        else:
            self.salary=10000
    def printdata(self):
        print("Name = ",self.name,"Id = ",self.id,"Salary = ",self.salary)

a1=Emp()
a2=Emp()
a1.setdata()
a2.setdata()
a1.printdata()
a2.printdata()