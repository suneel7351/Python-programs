import matplotlib.pyplot as plt
import numpy as nm


# # x=nm.array([1,4,7,6,3])
# # y=nm.array([7,6,9,6,5])


# # if we not pass x then the index of y work as x array


# # plt.plot((y))


# # plt.plot(x,y)


# # Draw a line between two cooordinates 7,9 and 9,14

# # x=nm.array([7,9])
# # y=nm.array([9,14])

# # plt.plot(x,y)


# # Draw a square

# x1 = nm.array([4, 8, 8, 4, 4])
# x2 = nm.array([4, 4, 8, 8, 4])
# # plt.plot(x1,x2,marker=',')
# # plt.plot(x1,x2,marker='x')
# # plt.plot(x1,x2,marker='H')
# # plt.plot(x1,x2,marker='d')

# plt.xlabel("x line")
# plt.ylabel("y line")
# plt.title("graph",loc="left")
# plt.plot(x1, x2, 'o-r',ms=22,mec='b',mfc='b',linestyle="dotted",color='hotpink')
# plt.grid()


# write a program age and taken input of the bp of that person plot this data on the diagram
# write a program to display the comperative diagram of two person plot the throw out the day callory consumption.
# The risk assessmemnt of different different person acc to following  person
#  1-red line more risk(150+bp),2-blue line(120-150),3-green line(below 120)


# x = []
# y = []

# for i in range(0, 5):
#     age = int(input("Enter the age of person="))
#     bp = int(input("Enter the bp of that perosn="))

#     x.append(age)
#     y.append(bp)


# array1 = nm.array(x)
# array2 = nm.array(y)

# plt.xlabel("Age")
# plt.ylabel("Blood Pressure")

# # plt.plot(array1, array2)
# color = ["#ff9ff3", "#feca57", "#48dbfb", "#1dd1a1",
#          "#f368e0"]
# plt.scatter(array1, array2, color=color)
# plt.show()


# x = nm.array([6, 10, 14, 18, 22])
# p1 = nm.array([100, 300, 400, 200, 300])
# p2 = nm.array([50, 150, 200, 350, 200])

# # plt.plot(x,p1)
# # plt.plot(x,p2)
# color = ["#ff9ff3", "#feca57", "#48dbfb", "#1dd1a1",
#          "#f368e0"]
# plt.scatter(x, p1, color=color)
# plt.scatter(x, p2, color=color)

# plt.show()


# x=[]
# y=[]

# for i in range(0, 3):
#     name = str(input("Enter name...="))
#     bp = int(input("Enter bp of that perosn="))
#     x.append(name)
#     y.append(bp)

# array1 = nm.array(["suneel", "Aditya", "Abhi"])
# bp = [101, 142, 160]
# array2 = nm.array(bp)
# for x in array2:
#     if x in range(100, 120):
#         plt.plot(array1, array2, ls="--", c='g', marker='o', mec="g")
#     if x in range(120, 150):
#         plt.plot(array1, array2, ls="--", c='b', marker='o', mec="b")
#     if x > 150:
#         plt.plot(array1, array2, ls="--", c='r', marker='o', mec="r")


# plt.show()


# x = nm.array([5, 7, 8, 7, 2, 17, 2, 9, ])
# y = nm.array([99, 86, 87, 88, 111, 86, 103, 87, ])
# sizes = nm.array([20, 50, 100, 120, 140, 160, 180, 200])
# alpha = nm.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
# # plt.plot(x, y)
# color = ["#ff9ff3", "#feca57", "#48dbfb", "#1dd1a1",
#          "#f368e0", "#c8d6e5", "#222f3e", "#54a0ff"]
# # plt.scatter(x, y, color='#ff6b6b')
# plt.scatter(x, y, color=color, cmap="Blues", s=sizes, alpha=alpha)
# plt.colorbar()
# plt.show()

# plt.grid()
# plt.show()

# x = []
# k = 1
# sizes = np.array([20, 50, 100])
# for i in range(0, 3):
#     bp = int(input("Enter bp... = "))
#     x.append(bp)

# for j in x:
#     if j > 150:
#         # plt.plot(k, j, c='r', marker='o', ls=":")
#         plt.scatter(k, j, color="#ff6b6b")
#         # plt.bar(k, j)
#         # plt.barh(k, j, color="#ff6b6b",height=0.1)
#     if j in range(120, 150):
#         # plt.plot(k, j, c='b', marker='o', ls=":")
#         plt.scatter(k, j, color="#ff6b6b")
#         # plt.bar(k, j)
#         # plt.barh(k, j, color="#ff6b6b",height=0.1)
#     if j in range(100, 120):
#         # plt.plot(k, j, c='g', marker='o', ls=":")
#         plt.scatter(k, j, color="#ff6b6b")
#         # plt.bar(k, j)
#         # plt.barh(k, j, color="#ff6b6b",height=0.1)
#     k += 1

# plt.show()

# x = nm.array([1, 1, 1, 1, 2, 2, 2, 6, 7, 99, 88, 99, 4, 5, 55, 5])

# plt.hist(x)

# # plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.show()


# name = ["Suneel", "Ritik", "Aditya", "Gola"]
# marks = nm.array([7, 8, 18, 21])
# plt.bar(name, marks, color="#ff9ff3",width=0.2)
# plt.show()
y = nm.array([35, 25, 25, 15])
label = ["math", "python", "economics", "software"]
# plt.pie(y, labels=label)
colors = ["black", "hotpink", "b", "#4CAF50"]
# plt.pie(y, labels=label,colors=colors)
# plt.pie(y, labels=label,colors=colors,shadow=True)
explode = [0.2, 0, 0, 0]
plt.pie(y, labels=label, colors=colors, shadow=True, explode=explode,startangle=90)

plt.legend(title="subject")
plt.show()


