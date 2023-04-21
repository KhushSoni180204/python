import random
jk=[]
a=int(input("Enter number for list => "))
for i in range(1,a+1):
    lol=random.randint(-20,20)
    jk.append(lol)
print(jk)
jam=[]
for j in jk:
    if j>0:
        j=j*-1
        jam.append(j)
    else:
        j=j*-1
        jam.append(j)
print(jam)