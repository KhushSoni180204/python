import random
khush=[]
a=int(input("Enter number of list => "))
for i in range(1,a+1):
    x=random.randint(1,10)
    khush.append(x)
print(khush)
if khush==0:
    print("The list is empty")
else:
    print("The list has",a,"elements")
