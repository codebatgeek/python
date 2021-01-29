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

day = today.strftime("%a")

if day == 'Mon':
	fare = 100
elif day == 'Tue':
	fare = 100 
elif day == 'Wed':
	fare = 100
elif day == 'Thu':
	fare = 100
elif day == 'Fri':
	fare = 100               
elif day == 'Sat':
	fare = 60
elif day == 'Sun':
    fare = 80
print("fare:", fare)
