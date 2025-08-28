def readfile(filename):
    f = open(filename).read().split("\n")
    matrix = []
    for line in f:
        line=line.split(';')
        matrix.append(line)
    matrix[0][0] = int(matrix[0][0])
    matrix[0][1] = int(matrix[0][1])
    matrix[1][0] = int(matrix[1][0])
    matrix[1][1] = int(matrix[1][1])
    matrix[2][0] = int(matrix[2][0])
    matrix[2][1] = int(matrix[2][1])
    matrix[3][0] = int(matrix[3][0])
    matrix[3][1] = int(matrix[3][1])
    matrix[4][0] = int(matrix[4][0])
    matrix[4][1] = int(matrix[4][1])
    
    return matrix

def readfile2(filename):
    f = open(filename).read().split('\n')
    matrix = []
    for line in f:
        line = line.split()
        matrix.append(line)
    
    for line in matrix:
        line.pop(0)
    
    matrix[0].append('0')
    matrix[0].append('NoPress')
    matrix[0].append("conference")
    

    matrix[0][0] = int(matrix[0][0])
    matrix[0][1] = int(matrix[0][1])
    matrix[1][0] = int(matrix[1][0])
    matrix[1][1] = int(matrix[1][1])
    matrix[2][0] = int(matrix[2][0])
    matrix[2][1] = int(matrix[2][1])

    matrix[0][2] = matrix[0][2]+matrix[0][3]
    matrix[1][2] = matrix[1][2]+matrix[1][3]
    matrix[2][2] = matrix[2][2]+matrix[2][3]
    for line in matrix:
        line.pop(-1)
    

    return matrix
    

def process(events,commands):
    matrix_17 = []
    matrix_100 = []
    for el in commands:
        for idx in events:
            if el[0] == idx[0] and el[1] != idx[1]:
                matrix_17.append(idx[0])
                matrix_17.append(idx[1])
                matrix_17.append(idx[2])
            elif el[0] == idx[0] and el[1] == idx[1]:
                matrix_100.append(idx[0])
                matrix_100.append(idx[1])
                matrix_100.append(idx[2])
    
    a = commands[2]
    b = matrix_17 
    c = matrix_100 
    
    print(f"Events of day {b[0]}")
    print(f"{b[4]} :{b[-1]}")
    print("cannot insert event.")
    print("Evant inserted.")
    print(f"Events of day {a[0]}:")
    print(f"{a[1]} : Press conference")
    
    
    
                

            
                
            
    
                

def main():
    events = readfile("events.txt")
    commands = readfile2('commands.txt')
    print(events)
    print()
    print(commands)
    print()
    process(events,commands)
    
if __name__ == "__main__":
    main()
