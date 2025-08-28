import random as r

def create_tic_tac_game():

    game = [[[ ],['|'],[ ],['|'],[ ]],
            [['---------']],
            [[ ],['|'],[ ],['|'],[ ]],
            [['---------']],
            [[],['|'],[],['|'],[]]
            ]

    
    
       
    while True:

        row = int(input("Enter row(0,1,2): "))
        col = int(input("Enter column(0,1,2): "))

        row1 = r.randint(0,2)
        col1 = r.randint(0,2)
         


        if row > 2:
            continue
        
        else:
            if col > 2:
                continue
            else:
                if len(game[row*2][col*2]) != 0 : 
                    pass
                else:
                    game[row*2][col*2].append("O")

        if len(game[row1*2][col1*2]) == 0:
            game[row1*2][col1*2].append("X")


        for i in range(len(game)):
            for j in range(len(game[i])):
                print(" ".join(str(x) for x in game[i][j]),end=" ")
            print()

      
        print()
    
        winner = None
        
        # rows
        for i in range(len(game)):
             
            if len(game[i]) != 5:
                continue
            
            else:    
                if game[i][0] == game[i][2] == game[i][4] == ['O']:
                    winner = "USER"

                elif game[i][0] == game[i][2] == game[i][4] == ['X']:
                    winner = "PC"
                
                #columns
                else:

                    for j in range(len(game[i])):

                        if game[0][j] == game[2][j] == game[4][j] == ['O']:
                            winner = "USER"
                    
                        elif game[0][j] == game[2][j] == game[4][j] == ['X']:
                            winner = "PC"
                        
                        #diagonals
                        else:
                            i = 0
                            j = 0
                            if game[i][j] == game[i+2][j+2] == game[i+4][j+4] == ['O']:
                                winner = "USER"
                            
                            elif game[i][j] == game[i+2][j+2] == game[i+4][j+4] == ['X']:
                                winner = "PC"
                            
                            elif game[i][-j-1] == game[i+2][j+2] == game[i+4][j-5] == ['O']:
                                winner = "USER"
                            
                            elif game[i][-j-1] == game[i+2][j+2] == game[i+4][j-5] == ['X']:
                                winner = "PC"


        
        if winner == "PC" or winner == "USER":
           break
    
    print(f"Player {winner} wins the match") 

    print()    
        


create_tic_tac_game()