class student:
    def __init__(self,no,name):
        self.no=no
        self.name=name
    def printdata(self):
        print("No = ",self.no," Name = ",self.name)

s1=student(1,"rahil")
s2=student(2,"mansi")
s1.printdata()
s2.printdata()