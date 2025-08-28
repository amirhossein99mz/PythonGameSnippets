import random as r

def tic_tac_game():

    game = []

    for i in range(3):
        new = []
        for j in range(3):
            new1 = []
            new.append(new1)
        game.append(new)
    
    

    while True:

        row = int(input("Enter a number as row (0,1,2):"))
        col = int(input("Enter a number as col (0,1,2):"))
        
        row1 = r.randint(0,2)
        col1 = r.randint(0,2)


        if row > 2:
            continue

        elif row >= 0 and row <= 2:
            if col > 2:
                continue

            elif col >= 0 and col <= 2:
                
                if len(game[row][col]) != 0:
                    continue
                
                elif len(game[row][col]) == 0:
                    game[row][col].append("O")
        
       
        
        
        if len(game[row1][col1]) == 0:
            game[row1][col1].append("X")
        
            
        for i in range(len(game)):
            print(" ".join(str(x) for x in game[i]))
        
        
        winner = None
        for i in range(len(game)):
                
            #row
            j = 0
            if game[i][j] == game[i][j+1] == game[i][j+2] == ['O']:
                winner = "User"
                   
            elif game[i][j] == game[i][j+1] == game[i][j+2] == ['X']:
                winner = "PC"
                
                
            else:
                   
                #column
                i = 0
                j = 0
                if game[i][j] == game[i+1][j] == game[i+2][j] == ['O']:
                    winner = "User"
                
                elif game[i][j] == game[i+1][j] == game[i+2][j] == ['X']:
                    winner = "Pc"
                
                
                
                elif game[i][j+1] == game[i+1][j+1] == game[i+2][j+1] == ['O']:
                    winner = "User"
                
                elif game[i][j+1] == game[i+1][j+1] == game[i+2][j+1] == ['X']:
                    winner = "Pc"
                


                elif game[i][j+2] == game[i+1][j+2] == game[i+2][j+2] == ['O']:
                    winner = "User"
                
                elif game[i][j+2] == game[i+1][j+2] == game[i+2][j+2] == ['X']:
                    winner = "Pc"
                
                
                else:
                      #diag
                    
                    if game[i][j] == game[i+1][j+1] == game[i+2][j+2] == ['X']:
                        winner = "PC"
                
                    elif game[i][j] == game[i+1][j+1] == game[i+2][j+2] == ['O']:
                        winner = "User"

                    elif game[i][-1-j] == game[i+1][j+1] == game[i+2][j] == ['X']:
                        winner = "PC"
                
                    elif game[i][-1-j] == game[i+1][j+1] == game[i+2][j] == ['O']:
                        winner = "User"   
                
            

                
        
        if winner != None :
            break
    print()
    print(f"{winner} wins the match")
    print()

tic_tac_game()