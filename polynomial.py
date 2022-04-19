# import numpy
# import matplotlib.pyplot as plt
# from sklearn import linear_model
# import pandas
# x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
# y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
# z = numpy.polyfit(x, y, 3)
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# myline = numpy.linspace(1, 22, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()
# print(z)


# multiple regression
import pandas
from sklearn import linear_model

df = pandas.read_csv("/project/bmi2.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
