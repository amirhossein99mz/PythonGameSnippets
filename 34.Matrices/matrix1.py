def create_matrixx():
    
    #diagonal matrix
    n = 5
    matrix = []
    p = n
    for i in range(n):
        new = []
        for j in range(n):
            if i != j:
                new.append(0)
            else:
                new.append(p)
        matrix.append(new)
        p = p-1
    
    for  i in range(len(matrix)):
        print(" ".join(str(x) for x in matrix[i]))

    print()
    #anti-diagonal matrix
    n = 5
    matrix = []
    p = n
    for i in range(n):
        new = []
        for j in range(n):
            new.append(0)
        matrix.append(new)
    
    p = n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][-1-i] = p

        p = p-1   
    
    for  i in range(len(matrix)):
        print(" ".join(str(x) for x in matrix[i]))

    print()

    #diagonal matrix2
    n = 5
    matrix3 = []
    p = n
    for i in range(n):
        new = []
        for j in range(n):
            if i > j:
                new.append(0)
            else:
                new.append(p)
        matrix3.append(new)
        p = p-1
    
    for  i in range(len(matrix3)):
        print(" ".join(str(x) for x in matrix3[i]))

    print()


    #diagonal matrix3
    n = 5
    matrix3 = []
    
    for i in range(n):
        p = 5-i
        new = []
        for j in range(n):
            if i > j:
                new.append(0)
            else:
                new.append(p)
                p = p-1
        matrix3.append(new)
        
    
    for  i in range(len(matrix3)):
        print(" ".join(str(x) for x in matrix3[i]))

    print()


create_matrixx()