from datetime import datetime
now = datetime.now()
year=now.strftime("%Y")
print("Year:",year)
month = now.strftime("%m")
print("Month:",month)
day = now.strftime("%d")
print("Date:",day)
time = now.strftime("%H:%M:%S")
print("time:",time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Date and time:",date_time)