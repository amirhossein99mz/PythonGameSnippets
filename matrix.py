# MATRICES IN PYTHON
def read_mat_file(file_name):
    try:
        with open(file_name) as file:
            f = file.read().split("\n")
        
        matrix = []
        list1 = []

        for line in f:
            line = line.split(";")
            for el in line:
                el = el.split()
                el = [int(i) for i in el]
                if el == []:
                    continue
                else:
                    list1.append(el)
            matrix.append(list1)
            list1 = []
        return(matrix)
    
    except  OSError as err:
        print(err)


def separation(main_matrix):

    matrix3x4 = []
    matrix2x2 = []
    matrix2x4 = []
    matrix4x2 = []  
    for line in main_matrix:
        if line[0] == [2,2]:
            matrix2x2.append(line[1:]) 
        elif line[0] == [2,4]:
            matrix2x4.append(line[1:]) 
        elif line[0] == [3,4]:
            matrix3x4.append(line[1:]) 
        elif line[0] == [4,2]:
            matrix4x2.append(line[1:])

    #print(matrix2x2[0])  
    return matrix2x4,matrix3x4,matrix4x2,matrix2x2



def sum_matrix(matrix_n):

    if len(matrix_n) == 1:
        print(f"sum of {len(matrix_n[0])} x {len(matrix_n[0][0])} matrices size{len(matrix_n[0])*len(matrix_n[0])} is:")
        for i in range(len(matrix_n[0])):
            print(" ".join(str(x) for x in matrix_n[0][i]))
    
    elif len(matrix_n) == 2:
        result = []
        for i in range(len(matrix_n[0])):
            new = []
            for j in range(len(matrix_n[1][0])):
                new.append(matrix_n[0][i][j]+matrix_n[1][i][j])
            result.append(new)
        print(f"sum of matrices {len(matrix_n[0])} x {len(matrix_n[0][0])} size {len(matrix_n[0])*len(matrix_n[0][0])} is:")
        for i in range(len(result)):
            print(" ".join(str(x) for x in result[i]))
    

def product(matrix_n):

    
    if len(matrix_n) != 2:
        print("Not valid")
    
    elif len(matrix_n) == 2:
        matrix1 = matrix_n[0]
        matrix2 = matrix_n[0]
        
        if len(matrix1[0]) != len(matrix2):
            print("Cannot product")
        
        elif len(matrix1[0]) == len(matrix2):
            result = []
            for i in range(len(matrix1)):
                new = []
                for j in range(len(matrix2[0])):
                    element = 0
                    for k in range(len(matrix2)):
                        element += (matrix1[i][k]*matrix2[k][j])
                    new.append(element)
                result.append(new)
            print(f"product of matix {len(matrix1)} x {len(matrix1[0])} and matrix {len(matrix2[0])} x {len(matrix2[0])} are:")
            for i in range(len(result)):
                print(" ".join(str(x) for x in result[i]))


def main():
    main_matrix =read_mat_file("mat.txt")
    matrix2x4,matrix3x4,matrix4x2,matrix2x2 = separation(main_matrix)
    sum_matrix(matrix2x2)
    print()
    sum_matrix(matrix2x4)
    print()
    sum_matrix(matrix3x4)
    print()
    sum_matrix(matrix4x2)
    print()
    product(matrix2x2)
    print()
    product(matrix2x4)
    print()
    product(matrix3x4)
    print()
    product(matrix4x2)
    print()

    

if __name__ == "__main__":
    main()