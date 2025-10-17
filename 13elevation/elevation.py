def readAltitudeFile(filename):

    try:
        f = open(filename)
    except OSError as e:
        print(f"The erro is {e}")
    
    matrix = [list(map(int,line.split()))for line in f]
    
    f.close()

    return(matrix)

def isValid(matrix,row,col):
    
    if row < 0 or col < 0 or row > len(matrix)-1 or col >len(matrix[row])-1:
        return False
    return True

def isMaximum(matrix,row,col):

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if isValid(matrix,row+i,col+j) == True and matrix[row+i][col+j] > matrix[row][col]:
                return False
    return True

def main():

    altitude = readAltitudeFile("C:/Users/javan/OneDrive/Desktop/program/17.Done/elevation.txt")
    
    sum1 = 0
    count1 = 0

    for row in range(len(altitude)):
        for col in range(len(altitude[row])):
            if  isMaximum(altitude,row,col) == True and altitude[row][col] > 0:
                print(altitude[row][col],row,col)
                sum1 += altitude[row][col]
                count1 += 1
    

    if count1 == 0:
        print("there are no peaks.")
    
    else:
        print(f"Average height: {sum1/count1}")



if __name__ == "__main__":
    main()