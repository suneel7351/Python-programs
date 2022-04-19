a = int(input("Enter inital value of the progression : "))
d = int(input("Enter common difference of progression : "))
n = int(input("How much element you want in Arithmetic Progression series : "))

for i in range(a, a*n+1, d):
    print(i)
