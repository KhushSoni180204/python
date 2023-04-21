f1=open("C:\ShyamSir\\abc.txt","r")
while True:
    ch = f1.read(1)
    if ch!=' ':
        print(ch,end="")
    if not ch:
        break
f1.close()
print(ch)