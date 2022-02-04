import datetime
from datetime import timedelta

dob = datetime.datetime(2001, 5, 3)
today = datetime.datetime(2022, 2, 4)

diff = today-dob


age = diff//timedelta(365)

print(age)
