import random
d1={}
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
    else:
        print(k,"\t",v,"\tPASS")

print("*"*30)
print("1 for Pass")
print("2 for Fail")
op = int(input("Enter Option=>"))
if op==1:
    for k, v in d1.items():
        if v > 16:
            print(k, "\t", v, "\tPASS")
if op==2:
    for k, v in d1.items():
        if v<16:
            print(k,"\t",v,"\tFAIL")