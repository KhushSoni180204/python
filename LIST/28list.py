import random
khush=[]
a=int(input("Enter a number for list => "))
for i in range(1,a+1):
    x=random.randint(1,30)
    khush.append(x)
print(khush)
l=int(input("Enter position => "))
m=int(input("Enter value => "))
khush.insert(l,m)
print(khush)