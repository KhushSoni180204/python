f1=open("C:\ShyamSir\\abc.txt","r")
c=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==" ":
        c=c+1
f1.close()
print("Count = ",c)
