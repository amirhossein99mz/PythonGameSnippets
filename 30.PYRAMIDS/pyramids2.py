def read_pyramids(filename):
    try:
        with open(filename) as file:
            file1 = file.read().split("\n")
        matrix = []

        for line in file1:
            line = line.split()
            line = [int(i) for i in line]
            matrix.append(line)
        
        return matrix
    
    except OSError as err:
        print(err)

def find_top_hills(map):
    
    top = []
    average = 0
    sum1 = 0
    count = 0

    for i in range(len(map)):
        if i > 0 and i < len(map)-1:
            for j in range(len(map[i])):
                if j > 0 and j < len(map[i])-1:
                    if map[i][j] > map[i][j+1]:
                        if map[i][j] > map[i][j-1]:
                            if map[i][j] > map[i-1][j]:
                                if map[i][j] > map[i+1][j]:
                                    top.append([map[i][j],i,j])
                                    sum1 += map[i][j]
                                    count += 1
        elif i == len(map)-1:
            for j in range(len(map[i])):
                if map[i][j] > map[i][j-1]:
                    if map[i][j] > map[i][j+1]:
                        if map[i][j] > map[i-1][j]:
                            top.append([map[i][j],i,j])
                            sum1 += map[i][j]
                            count+=1

    
    
    
    average = sum1/count


    print("The top hills are ")
    for line in top:
        
        print(f"{line[0]} : (row:{line[1]}, col:{line[2]})")
    print()
    print("The average height is",end=" ")
    print(average)
    
    

    




def main():

    map = read_pyramids("map.txt")

    find_top_hills(map)


if __name__ == "__main__":
    main()