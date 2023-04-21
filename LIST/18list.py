import random
a=int(input("Enter number of elements in list => "))
khush=[]
for i in range(1,a+1):
    x=random.randint(1,50)
    khush.append(x)
print(khush)
print(khush[0]+khush[-1])