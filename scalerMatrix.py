n=3
def scalerOfMatrix(matrix,k):
    for i in range(n):
        for j in range(n):
            matrix[i][j]=matrix[i][j]*k



matrix=[[4,3,5],[7,9,2],[7,2,1]]
k=5

scalerOfMatrix(matrix,k)
 
for i in range(n):
    for j in range(n):
        print(matrix[i][j])