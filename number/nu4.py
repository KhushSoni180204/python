import random
a=int(input("Enter number of ques => "))
b=(input("Enter prefered operator => "))
for i in range(a):
    x = random.randint(1,40)
    y = random.randint(1,40)
    if(b=='+'):
        print("No1 =",x,"No2 =",y)
        add=int(input("Enter addition => "))
        if(add==(x+y)):
            print("True")
        else:
            print("false")
    elif (b == '-'):
        print("No1 =", x, "No2 =", y)
        sub = int(input("Enter subtraction => "))
        if (sub == x - y):
            print("True")
        else:
            print("false")
    elif (b == '*'):
        print("No1 =", x, "No2 =", y)
        mul = int(input("Enter multiplication => "))
        if (mul == x * y):
            print("True")
        else:
            print("false")
    elif (b == '/'):
        print("No1 =", x, "No2 =", y)
        div = int(input("Enter division => "))
        if (div == x / y):
            print("True")
        else:
            print("false")
    else:
        print("Enter proper operator")