def fib_sequence():
    fib = [0,1]
    num = int(input("Enter a number"))
    for i in range(num):
        fib.append(fib[-1]+fib[-2])
    print(fib)

fib_sequence()

def pascal_triangle(n):
    matrix = [[1]]
    
    for i in range(n):
        new = [1]
        for j in range(len(matrix[-1])-1):
            new.append(matrix[-1][j]+matrix[-1][j+1])
        new.append(1)
        matrix.append(new)
    
    for i in range(len(matrix)):
        print(" ".join(str(x) for x in matrix[i]))

pascal_triangle(4)