khush=[1,3,5,7,8,4,8,8,9]
i=0
cnt=0
for i in khush:
    if i==8:
        cnt+=1
        print(i)
    else:
        print(i)
print(cnt,"total number of 8 in list")