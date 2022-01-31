def square(x):
    return x**2
def pow(x,y):
    return x**y



def sub(mat1,mat2,result):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j]=mat1[i][j]-mat2[i][j]


def sum(mat1,mat2,result):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j]=mat1[i][j]+mat2[i][j]
            
            
def mul(mat1,mat2,result):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j]=mat1[i][j]*mat2[i][j]           
