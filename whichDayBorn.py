import datetime


dob = datetime.datetime(2001, 5, 3)

day = dob.strftime("%A")

print("Person was born {}".format(day))
