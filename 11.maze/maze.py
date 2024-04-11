def readfile(filename):
    try:
        f = open(filename)
    except OSError as e:
        print(f"The error is {e}")
    
    maze = f.read().split("\n")

    return(maze)

def findCoordiantion(maze):
    cor = {}

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == ".":
                nei = []

                #check up
                if row > 0 and maze[row-1][col] == ".":
                    nei.append((row-1,col))

                #check down
                if row < len(maze)-1 and maze[row+1][col] == ".":
                    nei.append((row+1,col))

                #check right
                if col < len(maze[row])-1 and maze[row][col+1] == ".":
                    nei.append((row,col+1))

                #check left
                if col > 0  and maze[row][col-1] == ".":
                    nei.append((row,col-1))

                cor[(row,col)] = nei
    return cor


def main():
    maze = readfile("C:/Users/javan/OneDrive/Desktop/program/19.Done/maze.txt")
    cor = findCoordiantion(maze)
    
    for key,value in cor.items():
        print(f"{key} {value}")

if __name__ == "__main__":
    main()
