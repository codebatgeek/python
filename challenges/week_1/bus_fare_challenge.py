#Solution
from datetime import date
today = date.today()

#date
date = today.strftime("%Y-%m-%d")
print("date:", date)

#day
day = today.strftime("%a")
print("day:",day)

#fare

if today.strftime("%a") == 'Mon', 'Tue', 'Wed', 'Thu', 'Fri':
	fare = 100
elif today.strftime("%a") == 'Sat':
	fare = 60
elif today.strftime("%a") == 'Sun':
    fare = 80
else:
	print("day is not valid")
print("fare:", fare)
