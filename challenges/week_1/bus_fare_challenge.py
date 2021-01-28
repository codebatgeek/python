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

if today == 'Mon':
	fare = 100
elif today == 'Tue':
	fare = 100 
elif today == 'Wed':
	fare = 100
elif today == 'Thu':
	fare = 100
elif today == 'Fri':
	fare = 100               
elif today == 'Sat':
	fare = 60
else:
    fare = 80
print("fare:", fare)
