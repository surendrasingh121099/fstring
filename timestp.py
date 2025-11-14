import time
timestamp = time.strftime('%H:%M:%S')
if timestamp>'06:00:00' and timestamp<'12:00:00':
    print("Good Morning")
elif timestamp>'12:00:00' and timestamp<'18:00:00':
    print("Good Afternoon")
elif timestamp>'18:00:00' and timestamp<'21:00:00':
    print("Good Evening")
else:
    print("Good Night")
print("Current Time is :", timestamp)