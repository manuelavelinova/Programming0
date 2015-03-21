import time

today = time.strftime("%A")

print(today)

if today == "Friday":
    print("Today is Friday ")
else:
    print("Today is not Friday.Today is " + today)
