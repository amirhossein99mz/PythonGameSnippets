import random as r

def create_matrix():

    


    row = int(input("Enter a number as row:"))
    col = int(input("Enter a number as column:"))

    matrix = []

    for i in range(row):
        new = []
        for j in range(col):
            z = r.randint(1,9)
            new.append(z)
        matrix.append(new)

    for i in range(len(matrix)):
        print(" ".join(str(x)for x in matrix[i]))
    
    main_diag = [matrix[i][i] for i in range(min(row,col))]
    against_main_diag = [matrix[i][-1-i] for i in range(min(row,col))]

    first_col = [row[0] for row in matrix]
    last_col = [row[-1]  for row in matrix] 
    
    print()
    print(first_col)
    print()
    print(last_col)

    count = 0
    sum1 = []
    sum2 = []

    print()
    columns = []
    for i in range(len(matrix)):
        col1 = [row[i] for row in matrix]
        columns.append(col1)
        col1 = []
    
    count = 0
    sum1 = []
    for i in range(len(columns)):
        for j in range(len(columns[i])):
            count += columns[i][j]
        sum1.append(count)
        count = 0
    print(sum1)




create_matrix()