import random

x = random.randint(1, 30)
z = 0
cnt = 0
m=1
n=30
while z != x:
    z = int(input("Guess a number between",m,"to",n)
    cnt += 1
    if (z < x):
        m=z
        print("Guess a greater number than => ", z)
        print("Now your Range is between ",m,"to",n)
    elif (z > x):
        n=z
        print("Guess a smaller number than => ", z)
        print("Now your Range is between ", m, "to", n)
    else:
        print("you have guessed correct number => ", x)
        break
print("you have guessed ", cnt)
