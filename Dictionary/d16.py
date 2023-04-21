d1={"Ram":1,"Khush":2,"Zenil":3,"Khushi":4,"Mihir":5}
print(d1)
a=input("Enter the name to check => ")
m=0
for k,v in d1.items():
    if a==k:
        m=1
        break
    else:
        m=2
if m==1:
    print("It is in d1")
elif m==2:
    print("It is not in d1")