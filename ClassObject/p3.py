class student:
    def __init__(self):
        self.no=0
        self.name=""
    def setdata(self):
        self.no=int(input("Enter eno =>"))
        self.name=input("Enter name =>")
    def printdata(self):
        print("No = ",self.no," Name = ",self.name)

s1=student()
s2=student()
s1.setdata()
s2.setdata()
s1.printdata()
s2.printdata()