import random
list=[]
n=0
a=int(input("Enter number of elements in list => "))
for i in range(1,a+1):
    x=random.randint(1,40)
    list.append(x)
print(list)
for j in list:
    n=j+n
print("The sum of list is => ",n)