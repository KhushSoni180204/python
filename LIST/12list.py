khush=[7,12,21,49,56,75]
i=0
cnt=0
for i in khush:
    if i%7==0:
        cnt+=1
        print(i,"is divisable by 7")
    else:
        print(i,"is not divisable by 7")

print("Total number div by 7 are => ",cnt)