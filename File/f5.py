f1=open("C:\ShyamSir\\abc.txt","r")
while True:
    ch=f1.read(1)
    if ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u':
        print(7,end="")
    else:
        print(ch,end="")
f1.close()