import datetime
from datetime import date, timedelta
x = datetime.datetime.now()
print(x.strftime("%A"))  # Friday
print(x.strftime("%a"))  # Fri
print(x.strftime("%w"))  # 5 no. of day in week (0 to 7)
print(x.strftime("%d"))  # Date of the month
print(x.strftime("%b"))  # Name of the month Feb
print(x.strftime("%B"))  # Name of the month February
print(x.strftime("%m"))  # No of the month (1 to 12)
print(x.strftime("%y"))  # year in sort 22
print(x.strftime("%Y"))  # year in sort 2022
print(x.strftime("%p"))  # AM/PM
print(x.strftime("%M"))  # minutes
print(x.strftime("%S"))  # Seconds
print(x.strftime("%f"))  # microseconds
print(x.strftime("%j"))  # Day no. of the year (1 to 366)
# week no. of the year (Starting of the week from sunday)
print(x.strftime("%U"))
# week no. of the year (Starting of the week from Monday)
print(x.strftime("%w"))
print(x.strftime("%c"))  # local version of the date time
print(x.strftime("%x"))  # local version of the date


y = datetime.datetime(2022, 2, 4)
z = datetime.datetime(2000, 2, 4, 11, 25, 25)
print(y)
print(z)
w = y-z

print(datetime.timedelta(434//365))
