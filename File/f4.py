f1=open("C:\ShyamSir\\abc.txt","r")
while True:
    ch=f1.read(1)
    if ch==ch.upper():
        print(ch.lower(),end="")
    else:
        print(ch.upper(),end="")
f1.close()
