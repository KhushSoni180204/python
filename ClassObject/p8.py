class ind:
    def  __init__(self):
        self.a = 0
    def setind(self):
        self.a=int(input("Enter 1 number = "))
    def printind(self):
        print("A = ",self.a)

class us(ind):
    def  __init__(self):
        self.b = 0
    def setusa(self):
        self.b = int(input("Enter 2 number = "))
    def printusa(self):
        print("B = ",self.b)
    def mult(self):
        print(self.a,"*",self.b,"=",self.a * self.b)

u1=us()
u1.setind()
u1.setusa()
u1.printind()
u1.printusa()
u1.mult()