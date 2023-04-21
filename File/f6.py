f1=open("C:\ShyamSir\\abc.txt","r")
c=0
o=0
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==ch.upper():
        c=c+1
        print(ch,end="")
    else:
        print(ch,end="")
        o=o
f1.close()
print("\nUpper = ",c)
print("Lower = ",o)
