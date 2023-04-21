import random
stu={}
a=int(input("Enter number of students = "))
for i in range(0,a):
    x=random.randint(1,30)
    lol=[]
    e=random.randint(1,30)
    f=random.randint(1,30)
    g=random.randint(1,30)
    lol.append(e)
    lol.append(f)
    lol.append(g)
    stu[x]=lol
print("Enter 1 for pass fail")
print("Enter 2 for highest")
print("Enter 3 for second highest")
q=int(input("Enter = "))
if q==1:
    for k,v in stu.items():
        e,f,g=v
        Total=sum(v)
        print("En.no = ",k,"\t","English = ",e,"Social = ",f,"Computer = ",g,"TOTAL = ",Total)
        if e<8 or f<8 or g<8:
            print("En.no = ",k," Fail :|")
        else:
            print("En.no = ",k," Pass :)")
elif q==2:
    l1=[]
    for k,v in stu.items():
        e,f,g=v
        Total=sum(v)
        l1.append(Total)
    momo=max(l1)
    print("En.no\tEnglish\tSocial\tComputer\tTOTAL\tp/f")
    for k,v in stu.items():
        m1,m2,m3=v
        Total=sum(v)
        if Total==momo:
            print("",k,"\t",m1,"\t",m2,"\t",m3,"\t",Total,"\t","pass")
elif q==3:
    l1=[]
    for k,v in stu.items():
        m1,m2,m3=v
        total=sum(v)
        l1.append(total)
    m=max(l1)
    max2=0
    print("\nRollno\tenglish\thindi\tss\tTotal\tp/f")
    print("*"*40)
    for k,v in stu.items():
        m1,m2,m3=v
        total=sum(v)
        if (total>max2 and total<m):
            max2=total
    print("", k, "\t", m1, "\t", m2, "\t", m3, "\t", max2, "\t", "pass")
    print("*"*40)
