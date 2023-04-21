import random
d1={}
cnt=0
lnt=0
a = int(input("Enter data=>"))
for i in range(1,a+1):
    k=random.randint(1,30)
    v=random.randint(1,50)
    d1[k]=v
print("*"*30)
print("No\tMark\tResult")
print("*"*30)
for k,v in d1.items():
    if v<16:
        print(k,"\t",v,"\tFail")
        cnt=cnt+1
    else:
        print(k,"\t",v,"\tPASS")
        lnt=lnt+1
print("Pass = ",lnt,"Fail = ",cnt)
print("*"*30)