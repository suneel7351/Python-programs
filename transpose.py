p = int(input("Enter no. of rows : "))
q = int(input("Enter no. of column : "))
print("Enter the element of matrix : ")
matrix = [[int(input()) for j in range(q)] for i in range(p)]

print("matrix : ")
for i in range(p):
    for j in range(q):
        print(format(matrix[i][j], "<5"), end="")
    print()

result = [[0 for j in range(p)] for i in range(q)]

for i in range(q):
    for j in range(p):
        result[i][j] = matrix[j][i]

print("Transpose of matrix")

for i in range(p):
    for j in range(q):
        print(format(result[i][j], "<5"), end="")
    print()
