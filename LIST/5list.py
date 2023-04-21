import random
list1=[]
n=int(input("Enter limit "))
for i in range(1,n+1):
    x = random.randint(-20, 40)
    list1.append(x)

print(list1)