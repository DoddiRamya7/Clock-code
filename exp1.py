#addition of matrix
'''from numpy import *
matrix1=([[1,2,3],[4,5,6],[7,8,9]])
matrix2=([[7,8,9],[4,5,6],[1,2,3]])
result=matrix1+matrix2
print(result)           
print("matrix1=",matrix1)
print("matrix2=",matrix2)'''

#addition of matrix another method
'''import numpy as np
matrix1=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2=np.array([[7,8,9],[4,5,6],[1,2,3]])
result=matrix1+matrix2
print(result)           
print("matrix1=",matrix1)
print("matrix2=",matrix2)'''

#addition of matrix when the input is given by user
'''def input_matrix(rows,cols):
    matrix = []
    print(f"enter the elments for a {rows}x{cols}matrix:")
    for i in range(rows):
        row = list(map(int,input(f"enter row{i+1}(space-separated values):").split()))
        matrix.append(row)
    return matrix

def add_matrices(matrix1,matrix2):
   result = []
   for i in range(len(matrix1)):
       row = []
       for j in range(len(matrix1[0])):
           row.append(matrix1[i][j] + matrix2[i][j])
       result.append(row)
   return result
rows = int(input("enter the number of rows:"))
cols = int(input("enter the number of columns:"))
print("matrix 1:")
matrix1 = input_matrix(rows , cols)
print("\nmatrix 2:")
matrix2 = input_matrix(rows,cols)
result = add_matrices(matrix1 , matrix2)
print("\nmatrix1:")
for row in matrix1:
    print(row)
print("\nmatrix2:")
for row in matrix2:
    print(row)

print("\nresult of matrix addition:")
for row in result:
    print(row)'''



#spiral matrix traversal by default
'''def generate_spiral_matrix(n):
    matrix = [[0]*n for k in range(n)]
    start_row, end_row = 0, n-1
    start_col, end_col = 0,n-1
    counter=1

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col , end_col + 1):
            matrix[start_row][i] = counter
            counter +=1
        start_row +=1
        for i in range(start_row, end_row +1):
            matrix[i][end_col] = counter
            counter +=1
        end_col -=1
        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                matrix[end_row][i] = counter
                counter +=1
            end_row -= 1
        if start_col <= end_col:
            for i in range(end_row , start_row -1, -1):
                matrix[i][start_col] = counter
                counter +=1
            start_col +=1

    return matrix
n=int(input("enter the sixe of the spiral"))
spiral_matrix = generate_spiral_matrix(n)
print("spiral matrix:")
for row in spiral_matrix:
    print(row)'''



#spiral matrix when the input is given by user
'''def spiral_traversal(matrix,n):
    start_row, end_row = 0, n-1
    start_col, end_col = 0,n-1
    result = []

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col , end_col + 1):
            result.append(matrix[start_row][i])
        start_row +=1
        for i in range(start_row, end_row +1):
            result.append(matrix[i][end_col])
        end_col -=1
        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                result.append(matrix[end_row][i])
            end_row -= 1
        if start_col <= end_col:
            for i in range(end_row , start_row -1, -1):
                result.append(matrix[i][start_col])
            start_col +=1

    return result
n=int(input("enter the sixe of the matrix (nxn):"))
matrix = []
print("enter ths matrix row-wise:")
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
spiral_order = spiral_traversal(matrix,n)
print("\nspiral order transversal:")
print(spiral_order)'''








           