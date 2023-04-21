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
l1=[]
for i in range(0,101):
    l1.append('_')

while p1<100 and p2<100:
    dice=random.randint(1,6)
    if t%2==0:
        a=int(input(blue+"Player A turn enter 1 to roll the dice "))
        if a==1:
            p1=p1+dice
            print(p1)
            if l1[p1]=='_':
                l1[p1]='p1'
                print(p1,'p1')
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
            if l1[p2]=='_':
                l1[p2]='p2'
                print(p2,'p2')
        print(dice,"wow")
        if p2 in ladder:
            v=ladder[p2]
            p2=v
            print(green+"you got ladder")
        elif p2 in snake:
            v=snake[p2]
            p2=v
            print(red+"you are bitten by snake")
    print("| ", l1[100], " | ", l1[99], " | ", l1[98], " | ", l1[97], " | ", l1[96], " | ", l1[95], " | ", l1[94], " | ",
          l1[93], " | ", l1[92], " | ", l1[91], " |")
    print("| ", l1[81], " | ", l1[82], " | ", l1[83], " | ", l1[84], " | ", l1[85], " | ", l1[86], " | ", l1[87], " | ",
          l1[88], " | ", l1[89], " | ", l1[90], " |")
    print("| ", l1[80], " | ", l1[79], " | ", l1[78], " | ", l1[77], " | ", l1[76], " | ", l1[75], " | ", l1[74], " | ",
          l1[73], " | ", l1[72], " | ", l1[71], " |")
    print("| ", l1[61], " | ", l1[62], " | ", l1[63], " | ", l1[64], " | ", l1[65], " | ", l1[66], " | ", l1[67], " | ",
          l1[68], " | ", l1[69], " | ", l1[70], " |")
    print("| ", l1[60], " | ", l1[59], " | ", l1[58], " | ", l1[57], " | ", l1[56], " | ", l1[55], " | ", l1[54], " | ",
          l1[53], " | ", l1[52], " | ", l1[51], " |")
    print("| ", l1[41], " | ", l1[42], " | ", l1[43], " | ", l1[44], " | ", l1[45], " | ", l1[46], " | ", l1[47], " | ",
          l1[48], " | ", l1[49], " | ", l1[50], " |")
    print("| ", l1[40], " | ", l1[39], " | ", l1[38], " | ", l1[37], " | ", l1[36], " | ", l1[35], " | ", l1[34], " | ",
          l1[33], " | ", l1[32], " | ", l1[31], " |")
    print("| ", l1[21], " | ", l1[22], " | ", l1[23], " | ", l1[24], " | ", l1[25], " | ", l1[26], " | ", l1[27], " | ",
          l1[28], " | ", l1[29], " | ", l1[30], " |")
    print("| ", l1[20], " | ", l1[19], " | ", l1[18], " | ", l1[17], " | ", l1[16], " | ", l1[15], " | ", l1[14], " | ",
          l1[13], " | ", l1[12], " | ", l1[11], " |")
    print("| ", l1[1], " | ", l1[2], " | ", l1[3], " | ", l1[4], " | ", l1[5], " | ", l1[6], " | ", l1[7], " | ",
          l1[8], " | ", l1[9], " | ", l1[10], " |")
    t=t+1
if p1>100:
    print("Player A is winner")
else:
    print("Player B is winner")