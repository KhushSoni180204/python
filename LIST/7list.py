import random
cnt=0
cnt1=0
lol=0
list1=[]
n=int(input("Enter limit "))
for i in range(1,n+1):
    x = random.randint(-20, 40)
    list1.append(x)

print(list1)

for x in list1:
    lol=lol+x
    if x%2==0:
        cnt+=1
        print(x,"is even")
    else:
        cnt1+=1
        print(x,"is odd")
print("odd numbers is",cnt1)
print("even number is",cnt)
print("sum =",lol)