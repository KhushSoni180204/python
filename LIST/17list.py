import random
a=int(input("Enter number of elements in list => "))
khush=[]
n=0
k=0
for i in range(1,a+1):
    x=random.randint(1,50)
    khush.append(x)
print(khush)
for j in khush:
    if j>n:
        n=j
    elif j<n:
        j=n
print(n," is the greatest value in list")
for k in khush:
    if n>k:
        n=k
    elif k<n:
        n=k
print(n," is the smallest value in list")
