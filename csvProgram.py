# importing csv
import csv
from matplotlib import pyplot as plt
# include .csv file
filename = "suneel1.csv"

# initializing the rows list

rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # extracting each row
    for row in csvreader:
        rows.append(row)
print("total no. of rows {}".format(csvreader.line_num))


print('\nData rows are:\n')
for row in rows:
    for column in row:
        print("%10s" % column, end=" "),
    print('\n')
print(rows)