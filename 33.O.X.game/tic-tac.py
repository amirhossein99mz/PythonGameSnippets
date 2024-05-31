def read_file(filename):
    try:
        matrix = []
        with open(filename) as file1:
            for line in file1:
                line = line.strip().split()
                line[1] = int(line[1])
                line[2] = int(line[2])
                matrix.append(line)
        return matrix
    
    except OSError as err:
        print(err)


def tic_tac(moves):
    
    row = 3
    col = 3
    game = []
    for i in range(row):
        new = []
        for j in range(col):
            new.append("-")
        game.append(new)
    

    
    count = 0
    while True:
        for line in moves:
            symbol = line[0]
            row1 = line[1]
            col1 = line[2]
            
            if row1 < 0 or row1 > len(game)-1:
                pass
            else:
                if col1 < 0 or col1 > len(game)-1:
                    pass
                else:
                    if game[row1][col1] == "-":
                        game[row1][col1] = symbol
            count += 1
            
            if count <= 6:
                if symbol == "O":
                    print("Player 1 moves:")
                else:
                    print("Player 2 moves:")
                
                for i in range(len(game)):
                    print(" ".join(str(x) for x in game[i]))
            else:
                pass
        winner = None
        for i in range(len(game)):
            #check columns
            if i == 1:
                for j in range(len(game)):
                    if game[i-1][j] == game[i][j] == game[i+1][j] == "O":
                        winner = "Player 1"
                    elif game[i-1][j] == game[i][j] == game[i+1][j] == "X":
                        winner = "Player 2"
                    
            #check rows
            j = 1
            if game[i][j-1] == game[i][j] == game[i][j+1] == "O":
                winner ="Player 1"
            elif game[i][j-1] == game[i][j] == game[i][j+1] == "X":
                winner ="Player 2"
        
            # check main daigonal
            i = 1
            if game[i-1][i-1] == game[i][i] == game[i+1][i+1] == "O":
                winner = "Player 1 "
            elif game[i-1][i-1] == game[i][i] == game[i+1][i+1] == "X":
                winner = "Player 2 "
            else:
                #check anti diagonal
                if game[i-1][i-2] == game[i][i] == game[i+1][i-4] == "O":
                    winner = "Player 1 "
                elif game[i-1][i-2] == game[i][i] == game[i+1][i-4] == "X":
                    winner = "Player 2 "

        if winner != None:
            break
    
    print()
    print(f"Player {winner} wins the match after {count-5} moves")


def main():
    moves = read_file("moves.txt")
    tic_tac(moves)

if __name__ =="__main__":
    main()

