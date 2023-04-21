import random
x=random.randint(1,50)
z=0
cnt=0
while z!=x:
    z=int(input("Guess a number => "))
    cnt+=1
    if(z<x):
        print("Guess a greater number than => ",z)
    elif(z>x):
        print("Guess a smaller number than => ",z)
    else:
        print("you have guessed correct number => ",x)
        break
print("you have guessed ",cnt)
                                                