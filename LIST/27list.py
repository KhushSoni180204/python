import random
khush=[]
a=int(input("Enter a number for list => "))
for i in range(1,a+1):
    x=random.randint(1,30)
    khush.append(x)
print(khush)
for j in khush:
    if j%2==0:
        khush.remove(j)
print(khush)