import datetime


today = datetime.datetime.now()
day = today.strftime("%A")


if day == "Sunday":
    print("Today is sunday")

else:
    print("Today is {}".format(day))
