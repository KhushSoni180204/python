import random
snake={97:1,35:20,81:8,17:5,50:26}
ladder={5:8,3:22,11:26,20:29,89:99,57:77}
p1=0
p2=0
a=0
b=0
lol=0
lol1=0
for i in range(1,100):
    if i%2==0:
        lol=int(input("Player A turn enter 1 to roll the dice "))
        if lol==1:
            a=random.randint(1,6)
            p1=p1+a
        print(a,"wow")
        print("you are at",p1,"position")
        if p1>100:
            print("Player A is winner")
            break
    else:
        lol1 = int(input("Player B turn enter 2 to roll the dice "))
        if lol1==2:
            b=random.randint(1, 6)
            p2=p2+b
        print(b,"wow")
        print("you are at",p2,"position")
        if p2>100:
            print("Player B is winner")
            break