import time
a=time.localtime(time.time())
print("Current time =","Hour:",a.tm_hour,"Min:",a.tm_min,"Sec:",a.tm_sec)
if a.tm_hour <= 12:
    print("Mornin")
elif a.tm_hour <= 20:
    print("Evnin")
else:
    print("Night")