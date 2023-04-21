khush=(1,2,4,7,14,21,43,28,67)
sum=0
c=0
for i in khush:
    if i%7==0:
        sum=sum+i
        c=c+1
        print(i,"is divisible by 7")
print("sum is = ",sum)
print("count is = ",c)