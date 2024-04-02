matrix = [[1,2],
          [4,5]]


first_col = [row[0] for row in matrix]
last_col = [row[-1] for row in matrix]
print(matrix)
print(first_col)
print(last_col)

main_diag = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if i==j]
print(main_diag)

sub_diag = [matrix[-i][-i-1] for i in range(len(matrix))]

print(sub_diag)