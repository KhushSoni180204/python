import time
a=time.localtime(time.time())
print("Current time =","Hour:",a.tm_hour,"Min:",a.tm_min,"Sec:",a.tm_sec)
h= a.tm_hour
if h>12:
    h=h-12
    print(h,"pm")
else:
    print(h,"am")
