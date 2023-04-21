lmao=(1,2,3,4,5,6,7,8,9,0)
print(lmao)
s=0
a=int(input("Enter a value for search => "))
for i in lmao:
    if a==i:
        print(a,"is in tuple")
        s=1
if s==0:
    print(a,"is not a tuple")
