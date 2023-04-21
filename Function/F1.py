def add():
    a=int(input("enter first number=>"))
    b=int(input("enter second number=>"))
    print("add=",a+b)

def table():
    a=int(input("enter the number=>"))
    for i in range(1, 11):
        print(a, "X", i, "=", a * i)

def oe():
    a=int(input("enter the number=>"))
    if a%2==0:
        print(a,"is even")
    else:
        print(a, "is odd")

def max2():
    a=int(input("enter first number=>"))
    b=int(input("enter second number=>"))
    if a>b:
        print(a,"is max")
    else:
        print(b, "is max")

def pn():
    a=int(input("enter first number=>"))
    if a>0:
        print(a,"is positive")
    elif a==0:
        print(a,"is positive")
    else:
        print(a,"is negative")

def cube():
    a=int(input("enter first number=>"))
    print("cube is=>",a*a*a)

def areaoftri():
    h=int(input("enter height=>"))
    b=int(input("enter base=>"))
    print("area of triangle=>",h*b*0.5)

def areaofcircle():
    r=int(input("enter radius=>"))
    print("area of circle=>",3.14*r*r)

add()
table()
oe()
max2()
pn()
cube()
areaoftri()
areaofcircle()