import time
a=time.localtime(time.time())
print("Hour:",a.tm_hour)
if a.tm_hour <= 12:
    print("AM")
else:
    print("PM")