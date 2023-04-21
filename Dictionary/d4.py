import random
d1={}
a=int(input("Enter the value => "))
for i in range(1,a+1):
    k=random.randint(1,30)
    v=random.randint(1,50)
    d1[k]=v
print(d1)