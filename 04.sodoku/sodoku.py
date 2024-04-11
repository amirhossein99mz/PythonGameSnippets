def read_sodoku_table(file_name):
    try:
        with open(file_name) as file:
            f = file.read().split("\n")
        
        matrix = []
        for line in f:
            line = line.split(",")
            line = [int(i) for i in line]
            matrix.append(line)
        
        return matrix
    
    except OSError as err:
        print(err)


def calculation_sum(sodoku):
    

    #check each row
    
    count_row = 0
    sum_rows = []
    

    for i in range(len(sodoku)):
        for j in range(len(sodoku[i])):
            count_row += sodoku[i][j]
        sum_rows.append(count_row)
        count_row = 0

    sum_first_row = sum_rows[0]
    sum_rows.pop(0)

    

    count_column = 0
    sum_columns = []

    for j in range(len(sodoku[0])):
        columns = [row[j] for row in sodoku]
        for el in columns:
            count_column += el
        sum_columns.append(count_column)
        count_column = 0
    
    sum_first_column = sum_columns[0]
    sum_columns.pop(0)
    

    return sum_rows,sum_columns,sum_first_column,sum_first_row


def print_result(sum_rows,sum_columns,sum_first_column,sum_first_row):

    result_row = None

    for el in sum_rows:
        if el != sum_first_row:
            result_row = "NO"
        elif el == sum_first_row:
            result_row = "YES"

    
    result_column = None

    for el in sum_columns:
        if el != sum_first_column:
            result_column = "NO"
        elif el == sum_first_column:
            result_column = "YES"
    
    
    if result_row != result_column:
        print("This table is NOT sodoku.")
    
    if result_row == result_column:
        if result_row == "NO":
            print("This table is NOT sodoku.")

        elif result_row == "YES":
            print("This table is sodoku.")


def main():
    
    sodoku = read_sodoku_table("sodoku.txt")
    sum_rows,sum_columns,sum_first_column,sum_first_row = calculation_sum(sodoku)
    print_result(sum_rows,sum_columns,sum_first_column,sum_first_row)

if __name__ == "__main__":
    main()