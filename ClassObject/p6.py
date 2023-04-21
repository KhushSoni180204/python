class emp:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.salary = 0
    def setdata(self):
        self.name = input("Enter your name = ")
        self.id = int(input("Enter your id = "))
        self.salary = int(input("Enter your salary = "))
    def printdata(self):
        print("Name = ",self.name," Id = ",self.id," Salary = ",self.salary)


list1=[]
n=int(input("Enter limit =>"))
for x in range(1,n+1):
    e1=emp()
    e1.setdata()
    list1.append(e1)

for x in list1:
    x.printdata()

print("*"*20)
print("Salary greater than 10000")
print("*"*20)
for x in list1:
    if x.salary > 10000:
        x.printdata()
