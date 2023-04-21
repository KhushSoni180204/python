class stu:
    def __init__(self):
        self.name = ""
        self.Roll = 0
        self.Emarks = 0
        self.Mmarks = 0
        self.t = 0
    def setdata(self):
        self.name = input("Enter student name = ")
        self.Roll = int(input("Enter student Roll no = "))
        self.Emarks = int(input("Enter your English marks from 50 = "))
        self.Mmarks = int(input("Enter your Maths marks from 50 = "))
        self.t = self.Mmarks + self.Emarks
    def printdata(self):
        print("Name = ",self.name," Roll_no = ",self.Roll)
        print("English = ",self.Emarks," Maths = ",self.Mmarks)
        print("*"*10)

list1=[]
n = int(input("Enter limit => "))
for i in range(1,n+1):
    a1 = stu()
    a1.setdata()
    list1.append(a1)

for x in list1:
    if x.Emarks < 18 or x.Mmarks < 18:
        print("Student Failed")
        x.printdata()
    else:
        print("Student Passed")
        x.printdata()

for a in list1:
    x = a.t
    if x > a.t:
        x = a.t

q=0
for y in list1:
    if y.t>q:
        q=y.t
    elif y.t<q:
         y.t=q

print("-"*20)
print("Highest marks = ",q)
print("Lowest marks = ",x)