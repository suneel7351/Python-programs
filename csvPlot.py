# importing the csv module
import csv
from matplotlib import pyplot as plt

# open the file in read mode
filename = open('suneel1.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
Name = []
RollNo = []
Age = []

# iterating over each row and append
# values to empty list
for column in file:
    Name.append(column['Roll No.'])
    RollNo.append(column['Name'])
    Age.append(column['Age'])

# printing lists
print('Name:', Name)
print('Roll No:', RollNo)
print('Age:', Age)

plt.figure()
plt.plot(RollNo,Age)
plt.show()
