d1={"Ram":1,"Khush":2,"Zenil":3,"Khushi":4,"Mihir":5}
print(d1)
a=input("Enter the name to delete => ")
m=0
for k,v in d1.items():
    if a==k:
        m=1
        break
if m==1:
    d1.pop(k)
    print(d1)