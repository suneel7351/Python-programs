def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i]=matrix[i][j]




result=[[0,0,0],[0,0,0]]

matrix=[[1,2],[4,5],[7,8]]
transpose(matrix)
for i in result:
    print(i)
