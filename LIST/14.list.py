import random
khush=[]
a=int(input("Enter a value => "))
for i in range(a):
    x=random.randint(1,40)
    khush.append(x)
print(khush)
m=int(input("Enter a value => "))
j=khush.index(m)
print(j+1)