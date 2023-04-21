def add():
    a=int(input("Enter the first number = "))
    b=int(input("Enter the second number = "))
    print("Addition = ",a+b)
def sub():
    a=int(input("Enter the first number = "))
    b=int(input("Enter the second number = "))
    print("Substration = ",a-b)
def mul():
    a=int(input("Enter the first number = "))
    b = int(input("Enter the second number = "))
    print("Multiplication = ", a*b)
def dev():
    a = int(input("Enter the first number = "))
    b = int(input("Enter the second number = "))
    print("Division = ", a/b)
print("Enter 1 for +")
print("Enter 2 for -")
print("Enter 3 for *")
print("Enter 4 for /")
lol=int(input("Enter = "))
if lol==1:
    add()
elif lol==2:
    sub()
elif lol==3:
    mul()
elif lol==4:
    dev()
else:
    print("You are gay")