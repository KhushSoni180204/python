import random
ladder={1:38,4:14,8:30,21:42,28:76,50:67,71:92,80:99}
snake={32:10,34:6,48:26,62:18,88:24,95:56,97:78}
p1=0
p2=0
dice=0
a=0
b=0
t=0
red='\033[91m'
green='\033[32m'
blue='\033[34m'
yellow='\033[33m'
while p1<100 and p2<100:
    dice=random.randint(1,6)
    if t%2==0:
        a=int(input(blue+"Player A turn enter 1 to roll the dice "))
        if a==1:
            p1=p1+dice
            print(p1)
        print(dice,"wow")
        if p1 in ladder:
            v=ladder[p1]
            p1=v
            print(green+"you got ladder")
        elif p1 in snake:
            v=snake[p1]
            p1=v
            print(red+"you are bitten by snake")
    else:
        b=int(input(yellow+"Player B turn enter 2 to roll the dice "))
        if b==2:
            p2=p2+dice
            print(p2)
        print(dice,"wow")
        if p2 in ladder:
            v=ladder[p2]
            p2=v
            print(green+"you got ladder")
        elif p2 in snake:
            v=snake[p2]
            p2=v
            print(red+"you are bitten by snake")
    t=t+1
if p1>100:
    print("Player A is winner")
else:
    print("Player B is winner")