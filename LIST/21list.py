import random
l1=[]
a=int(input("Enter num for list => "))
for i in range(1,a+1):
    x=random.randint(1,5)
    l1.append(x)
print(l1)
for j in l1:
    if l1.count(j)>1:
        l1.remove(j)
print(l1)