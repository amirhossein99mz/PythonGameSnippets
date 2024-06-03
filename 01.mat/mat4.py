def read_file1(file_name):
    try:
        with open(file_name) as file1:
            file2 = file1.read().split("\n")
        
        mat = []
        for line in file2:
            new = []
            line = line.split(";")
            for el in line:
                el = el.split()
                el = [int(i) for i in el]
                if len(el) > 0:
                    new.append(el)
            if len(new) > 0:
                mat.append(new)
        
        for line in mat:
            line[1:] = [line[1:]]
        
        return mat

    except FileNotFoundError as err:
        print(err)

def sepaation_matrices(mat):

    
    print()
    matrix = []
    matrix2 = []
    for i in range(len(mat)):
        matrix.append(mat[i][0])
    
  
    matrix = matrix[0:3]

    
    matrix2 = []
    for i in range(len(matrix)):
        matrix2.append([matrix[i]])
    
    
    for i in range(len(mat)):
        for j in range(len(matrix2)):
            if mat[i][0] == matrix2[j][0]:
                matrix2[j].append(mat[i][1])
            else:
                if mat[i][0][0] == matrix2[j][0][1] and mat[i][0][1] == matrix2[j][0][0]:
                    matrix2[j].append(mat[i][1])
     
    mat2 = matrix2
    
    return mat2

def mutiplication_of_matrices(mat2):
    
    for t in range(len(mat2)):
        m2 = []
        for i in range(len(mat2[t][1])):
            new = []
            for j in range(len(mat2[t][2][0])):
                element = 0
                for k in range(len(mat2[t][2])):
                    element += (mat2[t][1][i][k] * mat2[t][2][k][i])
                new.append(element)
            m2.append(new)
        mat2[t].append(m2)
    
    for s in range(len(mat2)):
        print(f"products of matrices size {mat2[s][0][0]} x {mat2[s][0][0]} is :")
        for i in range(len(mat2[s][-1])):
            print(" ".join(str(x) for x in mat2[s][-1][i]))
        print()
    print()

    

def main():

    mat = read_file1("mat2.txt")
    mat2 = sepaation_matrices(mat)
    mutiplication_of_matrices(mat2)


if __name__ == "__main__":
    main()