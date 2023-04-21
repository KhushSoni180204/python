import random
lol=0
a=int(input("How much question you can answer"))
for i in range(a):
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    print("No1 = ",x,"No2 = ",y)
    add=int(input("Enter addition => "))
    if (add==x+y):
        print("True")
        lol=lol+1
    else:
        print("false")
print(lol,"question are correct")