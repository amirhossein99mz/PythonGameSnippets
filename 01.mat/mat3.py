def read_file(filename):
    try:
        with open(filename) as file1:
            file2 = file1.read().split("\n")
        mat = []

        for line in file2:
            new = []
            line = line.split(";")
            for el in line : 
                el = el.split()
                el = [int(i) for i in el]
                if len(el) == 0:
                    pass
                else:
                    new.append(el)
            mat.append(new)
        
        return mat

    except OSError  as err:
        print(err)


def separation_of_matrices(mat):
    
    

    matrix = []

    for i in range(len(mat)):
        if mat[i][0] in matrix:
            continue
        else:
            matrix.append(mat[i][0])
    

    mat2 = []

    for k in range(len(matrix)):
        mat2.append([matrix[k]])
    
    

    
    for i in range(len(mat)):
        mat[i][1:] = [mat[i][1:]]
    
    print()
    
    for i in range(len(mat2)):
        for j in range(len(mat)):
            if mat2[i][0] == mat[j][0]:
                mat2[i].append(mat[j][1])
    print()
    
    return mat2
                

def sum_of_matrices(mat2):
    
    
    for i in range(len(mat2)):
        print(mat2[i])
    
    print()

    for i in range(len(mat2)):
        if len(mat2[i]) < 3:
            pass
        else:
            m2 = []
            for j in range(len(mat2[i][1])):
                new = []
                for k in range(len(mat2[i][2][0])):
                    element = mat2[i][1][j][k] + mat2[i][2][j][k]
                    new.append(element)
                m2.append(new)
            mat2[i].append(m2)
    

    print()
    for i in range(len(mat2)):
        row = mat2[i][0][0]
        column = mat2[i][0][1]
        print(f"sum of matrices {row}x{column} is:")
        
        if len(mat2[i]) > 2:
            for j in range(len(mat2[i][-1])):
                for k in range(len(mat2[i][-1][j])):
                    print(mat2[i][-1][j][k],end=" ")
                print()
            print()
        else:
            for j in range(len(mat2[i][1])):
                for k in range(len(mat2[i][1][j])):
                    print(mat2[i][1][j][k],end=" ")
                print()
            print()
            

            



    
    
    

def main():
    
    mat = read_file("mat.txt")
    mat2 = separation_of_matrices(mat)
    sum_of_matrices(mat2)

if __name__ == "__main__":
    main()