
p = int(input("Enter no. of rows : "))
q = int(input("Enter no. of column : "))
k = int(input("Enter the value of k : "))
print("enter the element of matrix : ")
matrix = [[int(input()) for j in range(q)] for i in range(p)]

print("matrix")
for i in range(p):
    for j in range(q):
        print(format(matrix[i][j], "<6"), end="")
    print()
for i in range(p):
    for j in range(q):
        matrix[i][j] = matrix[i][j]*k

print("Scaler matrix : ")

for i in range(p):
    for j in range(q):
        print(format(matrix[i][j], "<6"), end="")
    print()
