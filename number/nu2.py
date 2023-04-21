import random
x=random.randint(1,40)
y=random.randint(1,40)
print("No1 = ",x," No2 = ",y)
add=int(input("Enter addition =>"))
if (add==x+y):
    print("True")
else:
    print("False")
mul=int(input("Enter multiplacition =>"))
if (add==x*y):
    print("True")
else:
    print("False")
div=int(input("Enter Division =>"))
if (add==x/y):
    print("True")
else:
    print("False")
sub=int(input("Enter sub =>"))
if (add==x-y):
    print("True")
else:
    print("False")