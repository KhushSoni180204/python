import random
d1={}
a=int(input("Enter a value => "))
for i in range(1,a+1):
    k = random.randint(1, 30)
    v = random.randint(1, 50)
    d1[k] = v
for k,v in d1.items():
    if v<16:
        print("roll = ",k,"marks = ",v," Fail ")
    else:
        print("roll = ",k,"marks = ",v," Pass ")
