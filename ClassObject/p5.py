class bank:
    def __init__(self):
        self.name = ""
        self.Ac_no = 0
        self.branch = ""
        self.bb = 10000
    def setdata(self):
        self.name = input("Enter your name = ")
        self.Ac_no = int(input("Enter your Ac.no = "))
        self.branch = input("Enter your branch = ")
    def deposit(self):
        a = int(input("Enter your deposit amount = "))
        self.bb+=a
        print("Current bank balance = ",self.bb)23
    def withdraw(self):
        a = int(input("Enter your amount = "))
        self.bb-=a
        print("Current bank balance = ",self.bb)
    def printdata(self):
        print("Name = ",self.name,"Acc No = ",self.Ac_no,"Branch = ",self.branch)
        print("Your bank balance = ",self.bb)
a1=bank()
a1.setdata()
a = int(input("Enter 1 for deposit and 2 for withdraw and 3 for just cheak = "))
if a==1:
    a1.deposit()
elif a==2:
    a1.withdraw()
a1.printdata()