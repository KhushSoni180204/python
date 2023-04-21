khush=(1,2,3,4,5,6,7,8,9,10)
co=0
sum=0
for i in khush:
    if i%2==0:
        print(i,"is even")
        sum=sum+i
        co=co+1
print("sum is = ",sum)
print("count is = ",co)