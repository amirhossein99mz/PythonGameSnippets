def read_maze_file(filename):
    try:

        maze = []
        with open(filename) as file:
            f = file.read().split("\n")
        
        maze = f
        
        return maze

    except OSError as err:
        print(err)


def find_coordiantion_of_neighbours(maze):
    
    coor = {}

    for row in range(len(maze)):
        
        for col in range(len(maze[row])):
            if maze[row][col] == ".":
                new = []
                #check left
                if col > 0 and maze[row][col-1] == ".":
                    new.append((row,col-1))
                #check right
                elif col < len(maze[row])-1 and maze[row][col+1] == ".":
                    new.append((row,col+1))
                #check up
                if row > 0 and maze[row-1][col] == ".":
                    new.append((row-1,col))
                #check down
                elif row < len(maze)-1 and maze[row+1][col] == ".":
                    new.append((row+1,col))

                coor[(row,col)] = new
    
    return coor

        


def main():

    maze = read_maze_file("maze.txt")
    coor = find_coordiantion_of_neighbours(maze)
    
    for key,value in coor.items():
        print(key,value)

if __name__ == "__main__":
    main()