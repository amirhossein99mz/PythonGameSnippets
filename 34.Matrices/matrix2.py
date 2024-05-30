#transpose of matrix
#sum of two matrices
#product of two matrices
#column of matrices
#row of matrices


# transpose

import random as r

def transpose_matrix(matrix):


    row = len(matrix)
    col = len(matrix[0])
    matrix2 = []

    if row == col:
        for i in range(len(matrix)):
            new = []
            for j in range(len(matrix[0])):
                new.append(0)
            matrix2.append(new)
    else:
        for j in range(len(matrix[0])):
            new = []
            for i in range(len(matrix)):
                new.append(0)
            matrix2.append(new)



    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            matrix2[j][i] = matrix[i][j]

    return matrix2


#sum


def sum_matrices(matrix,matrix2):
    
    if len(matrix) != len(matrix2):
        return False
    else:
        if len(matrix[0]) != len(matrix2[0]):
            return False
        else:
            sum1 = []
            for i in range(len(matrix)):
                new = []
                for j in range(len(matrix2[0])):
                    element = matrix[i][j] + matrix2[i][j]
                    new.append(element)
                sum1.append(new)
            
    return sum1


#product

def product_matrices(matrix,matrix2):
    if len(matrix[0]) != len(matrix2):
        return False
    else:
        product = []
        for i in range(len(matrix)):
            new = []
            for k in range(len(matrix2[0])):
                element = 0
                for j in range(len(matrix2[0])):
                    element += (matrix[i][j]*matrix2[j][k])
                new.append(element)
            product.append(new)
    
    return product



#inverse 

def inverse1(matrix):
    
    matrix2 = [[0,0],[0,0]]
    
    if len(matrix) == len(matrix[0]) == 2:
        determinate = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])

        if determinate != 0:
        
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i == j:
                        matrix2[i][j] = matrix[j][i]
                        matrix2[i][j] = matrix2[i][j]
                    else:
                        matrix2[i][j] = -matrix[i][j]
                        matrix2[i][j] = matrix2[i][j]
        
            for i in range(len(matrix2)):
                for j in range(len(matrix2[0])):
                    matrix2[i][j] = (matrix2[i][j] * (1/determinate))
        
    return matrix2        



def main():

    row = int(input("Enter a number as row:"))
    col = int(input("Enter a number as column:"))

    matrix = []
    for i in range(row):
        new = []
        for j in range(col):
            z = r.randint(0,9)
            new.append(z)
        matrix.append(new)

    matrix2 = transpose_matrix(matrix)


        
    print("The original matrix is:")

    for i in range(len(matrix)):
        print(" ".join(str(x) for x in matrix[i]))
    
    print()
  
    print()
    print("The transpose of the  matrix is:")

    for i in range(len(matrix2)):
        print(" ".join(str(x) for x in matrix2[i]))

    print()
    
    if sum_matrices(matrix,matrix2):

        print("The sum of matrices is ")
        sum1 = sum_matrices(matrix,matrix2)
        for k in range(len(sum1)):
                print(" ".join(str(x) for x in sum1[k]))
    
    print()

    if product_matrices(matrix,matrix2):
        print("The product of matrices is ")
        product = product_matrices(matrix,matrix2)
        for j in range(len(product)):
                print(" ".join(str(x) for x in product[j]))

    print()

    
    inverse = inverse1(matrix)
    if inverse[0][0] == inverse[1][1] == inverse[0][1] == inverse[1][0] == 0:
        pass
    else:
        print("inverse of matrix is ")
        for i in range(len(inverse)):
            print(" ".join(str(x) for x in inverse[i]))
        
    

    #
    row1 = len(matrix)
    col1 = len(matrix[0])
    if row1 >= col1:
        min1 = col1
    else:
        min1 = row1
    
    
    main_diag = [matrix[i][i] for i in range(min1)]
    sub_diag = [matrix[i][-1-i] for i in range(min1)]
    
    columns = []

    for i in range(col1):
        column = []
        column = [row[i] for row in matrix]
        columns.append(column)
    

    print()
    print("main diagonal is ")
    print(main_diag)
 
    print()

    print()
    print("inverse of main  diagonal is ")
    print(sub_diag)
    print()

    print()
    print("columns are ")
    for i in range(len(columns)):
            print(" ".join(str(x) for x in columns[i]))
    print()



    # sort 


    for k in range(100):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j > 0:
                    if matrix[i][j-1] <= matrix[i][j]:
                        pass
                    else:
                        matrix[i][j-1],matrix[i][j] =  matrix[i][j],matrix[i][j-1]
                elif j < len(matrix[i]):
                    if matrix[i][j] <= matrix[i][j+1]:
                        pass
                    else:
                        matrix[i][j],matrix[i][j+1] =  matrix[i][j+1],matrix[i][j]

    print("sorted matrix is ")
    print(matrix)
    
    


if __name__ == "__main__":
    main()
    


