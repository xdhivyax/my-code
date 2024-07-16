matrix1=[
    [1,2,3],
    [3,4,6],
    [2,6,3]
]
for r in matrix1:
    print(r)
print()

matrix2=[
    [1,3,2],
    [2,4,1],
    [2,3,6]
]
for r in matrix2:
    print(r)
print()

result=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
for r in result:
    print(r)