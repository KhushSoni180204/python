import random
n=int(input("Enter limit => "))
list1=[]
for i in range(n):
    x = random.randint(1, 30)
    list1.append(x)
print("Total elements",list1)
listodd=[]
listeven=[]
for x in list1:
    if x%2==0:
        listeven.append(x)
    else:
        listodd.append(x)

print("List of odd elements = ",listodd)
print("List of even elements =",listeven)
