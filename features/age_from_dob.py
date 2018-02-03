#convert dob to age
from datetime import date

born = '30-10-1970'
day = int(born.split('-')[0])
month = int(born.split('-')[1])
year = int(born.split('-')[2])

print day,month,year

today = date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print age