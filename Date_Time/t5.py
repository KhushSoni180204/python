import time
a=time.localtime(time.time())
print("Current year is ",a.tm_year)
if a.tm_yday % 4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")