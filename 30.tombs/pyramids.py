def read_pyramid_file(file_name):

    try:
        with open(file_name) as file:
            matrix = [list(map(int,line.split()))for line in file]
        
        return(matrix)
    
    except OSError as err:
        print(err)

def is_valid(matrix,row,col):
    
    if row < 0 or col < 0 or row > len(matrix)-1 or col > len(matrix[row])-1:
        return False
    return True

def is_maximum(matrix,row,col):
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (i!=0 or j!=0) and is_valid(matrix,row+i,col+j) and matrix[row+i][col+j] >= matrix[row][col]:
                return False
    return True


def main():
    
    pyramid = read_pyramid_file("map.txt")

    count = 0
    sum1 = 0

    for row in range(len(pyramid)):
        for col in range(len(pyramid[row])):
            if is_maximum(pyramid,row,col) and pyramid[row][col] > 0:

                print(pyramid[row][col],row,col)
                
                sum1 += pyramid[row][col]
                count += 1
    
    if count == 0:
        print("There is No maxima")

    else:
        print(f"The average height is {sum1/count}")


if __name__ == "__main__":
    main()