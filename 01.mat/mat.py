def read_mat_file(filename):
    try:
        with open(filename) as file1:
            file = file1.read().split("\n")
        
        matrix = []
        for line in file:
            new = []
            line = line.split(";")
            for el in line:
                el = el.split()
                if len(el) > 0:
                    el = [int(i) for i in el]
                    new.append(el)
            matrix.append(new)
        for line in matrix:
            line[1:] = [line[1:]]
        
        return matrix
    
    except OSError as err:
        print(err)


def division_and_sum(matrix1):
    matrix = []

    for line in matrix1:
        if line[0] not in matrix:
            matrix.append([line[0]])
    
    matrix.pop(0)
    matrix.pop(1)
    matrix.pop(-1)

    for line in matrix1:
        for el in matrix:
            if line[0] == el[0]:
                el.append(line[1])

    for line in matrix:
        if len(line) == 2:
            pass
        else:
            line2 = []
            for i in range(len(line[1])):
                new = []
                for j in range(len(line[2][0])):
                    element = line[1][i][j] + line[2][i][j]
                    new.append(element)
                line2.append(new)
            line.append(line2)
    
    

    for i in range(len(matrix)):
        print(f"sum of matrices {matrix[i][0][0]} x {matrix[i][0][1]} is")
        for j in range(len(matrix[i][-1])):
            print(" ".join(str(x) for x in matrix[i][-1][j]))
        print()
def main():

    matrix1 = read_mat_file("mat.txt")
    division_and_sum(matrix1)
    
    

if __name__ == "__main__":
    main()
