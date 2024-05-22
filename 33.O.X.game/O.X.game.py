import random as r
def OX_game():
    game = [[[],[],[]],
            [[],[],[]],
            [[],[],[]]]


    while True:
        
        row1 = int(input("Enter a number as row (0,1,2):"))
        col1 = int(input("Enter a number as column (0,1,2):"))
        row2 = r.randint(0,2)
        col2 = r.randint(0,2)
        if row1 < 0 or row1 > 2:
            pass
        else:
            if col1 < 0 or col1 > 2:
                continue
            else:
                if len(game[row1][col1]) == 0:
                    game[row1][col1] = ["O"]
        
        if row2 < 0 or row2 > 2:
            pass
        else:
            if col2 < 0 or col2 > 2:
                continue
            else:
                if len(game[row2][col2]) == 0:
                    game[row2][col2] = ["X"]
        print("-----------------")
        for i in range(len(game)):
            for j in range(len(game[i])):
                if len(game[i][j]) != 0:
                    for k in range(len(game[i][j])):
                        print("|",game[i][j][k],"|",end=" ")
                
                else:
                    print("|","-","|",end=" ")
            print()
            print("-----------------")
        winner = None

        for i in range(len(game)):
            if game[i][0] == game[i][1] == game[i][2] == ["O"] :
                winner = "USER"
            
            elif game[i][0] == game[i][1] == game[i][2] == ["X"] :
                winner = "PC"
            
            else:
                for j in range(len(game)):
                    if game[0][j] == game[1][j] == game[2][j] == ["O"]:
                        winner = "USER"
                    elif game[0][j] == game[1][j] == game[2][j] == ["X"]:
                        winner = "PC"
                    else:
                        if i == 0:
                            if game[i][i] == game[i+1][i+1] == game[i+2][i+2]== ["O"]:
                                winner = "USER"
                            elif game[i][i] == game[i+1][i+1] == game[i+2][i+2]== ["X"]:
                                winner = "PC"
                            else:
                                if game[i][i-1] == game[i+1][i-2] == game[i+2][i-3]== ["O"]:
                                    winner = "USER"
                                elif game[i][i-1] == game[i+1][i-2] == game[i+2][i-3]== ["X"]:
                                    winner = "PC"
                        
    
        if winner == "PC" or winner == "USER":
            break
    
    print(winner)
         



OX_game()



















