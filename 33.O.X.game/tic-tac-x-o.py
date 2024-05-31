import random as r
def ox_game():
    #define a list
    matrix = [[[],[],[]],
              [[],[],[]],
              [[],[],[]]]
    
    # all operation should be done in a while True loop 
    while True:
        #inrtoude row & col for both user and pc

        #user
        row1 = int(input("Enter a number as row (0,1,2): "))
        col1 = int(input("Enter a number as column (0,1,2):"))
        
        #PC
        row2 = r.randint(0,2)
        col2 = r.randint(0,2)
        
        #row and col have to be in the range 0 to 2  for USER
        if row1 < 0 or row1 > 2:
            pass
        else:
            if col1 < 0 or col1 > 2:
                pass
            else:
                if len(matrix[row1][col1]) != 0:
                    pass
                else:
                    #add O as USER
                    matrix[row1][col1] = ['O']




        #row and col have to be in the range 0 to 2  for PC
        if row2 < 0 or row2 > 2:
                continue
        else:
            if col2 < 0 or col2 > 2:
                continue
            else:
                if matrix[row2][col2] != []:
                    continue
                else:
                    # add X as PC
                    matrix[row2][col2].append("X")

        #print each turn played by USER
        print("--------------")
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if len(matrix[i][j]) != 0:
                    for k in range(len(matrix[i][j])):
                        print("|",matrix[i][j][k],end=" ")
                else:
                    print("|","-",end=" ")
            print("|")
            
            print()
        print("-------------")
        

    
        #check rach row
        winner = None
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][0] == matrix[i][1] == matrix[i][2] == ['O']:
                    winner = "USER"
                elif matrix[i][0] == matrix[i][j] == matrix[i][2]==['X']:
                    winner = "PC"
                else:
                    #check columns
                    if matrix[0][j] == matrix[1][j] == matrix[2][j] == ['O']:
                        winner = "USER"
                    
                    elif matrix[0][j] == matrix[1][j] == matrix[2][j] == ['X']:
                        winner = "PC"
                    
                    else:
                        #check main diagonal
                        i = 0
                        if matrix[i][i] == matrix[i+1][i+1] == matrix[i+2][i+2] == ['O']:
                            winner = "USER"
                        elif matrix[i][i] == matrix[i+1][i+1] == matrix[i+2][i+2] == ['X']:
                            winner = "PC"
                        else:
                            #check anti-main diagonal
                            if matrix[i][i-1] == matrix[i+1][i-2] == matrix[i+2][i-3] == ['O']:
                                winner == "USER"
                            elif matrix[i][i-1] == matrix[i+1][i-2] == matrix[i+2][i-3] == ['X']:
                                winner == "PC"

        if winner != None:
            break

    print("winner is ",winner)                
        




ox_game()