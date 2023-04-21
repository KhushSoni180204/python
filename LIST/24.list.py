import random
khush=[]
a=int(input("Enter number for list => "))
for i in range(1,a+1):
    x=random.randint(1,15)
    khush.append(x)
print(khush)
v=int(input("Enter greater than value => "))
for j in khush:
    if j>v:
        print(j)