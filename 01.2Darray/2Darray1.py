def  read_mat_file(filename):
    try:
        with open(filename) as file1:
            file = file1.read().split("\n")
        
        matrix = []
        for line in file:
            new = []
            line = line.split(";")
            for el in line:
                el = el.split()
                el = [int(i) for i in el]
                if len(el) > 0:
                    new.append(el)
            matrix.append(new)
        

        for line in matrix:
            line[1:] = [line[1:]]
        

        return matrix

    
    except OSError as err:
        print(err)


def process(matrix1):

    
    matrix = []
    
    for line in matrix1:
        if line[0] not in matrix:
            matrix.append([line[0]])
    
    
    
    
    for i in range(len(matrix1)):
        for j in range(len(matrix)):
            if matrix1[i][0] == matrix[j][0]:
                matrix[j].append(matrix1[i][1])
    
    matrix.pop(0)
    matrix.pop(1)
    matrix.pop(-1)
    
    
    for i in range(len(matrix)):
        line2 = []
        if len(matrix[i]) == 2:
            pass
        else:
            for j in range(len(matrix[i][1])):
                new = []
                for k in range(len(matrix[i][2][0])):
                    new.append(matrix[i][1][j][k]+matrix[i][2][j][k])
                line2.append(new)
        matrix[i].append(line2)
    
    for i in range(len(matrix)):
        print(f"sum of matrix {matrix[i][0][0]} x {matrix[i][0][1]}  size {matrix[i][0][0] * matrix[i][0][1]}:")
        for t in range(len(matrix[i][-1])):
            print(" ".join(str(x) for x in matrix[i][-1][t]))           
        print()
def main():

    matrix1 = read_mat_file("mat.txt")

    process(matrix1)


if __name__ == "__main__":
    main()