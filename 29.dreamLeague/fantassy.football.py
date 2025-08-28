#The budget : 260 Millions .

#W. 20 Millions  goalkeepers, 40 for defenders, 80 to midfielders and 120 to forwards

#For each role, the program buys the most expensive footballer among those that meet the following two conditions:

#the player's price is less than or equal to the budget
#after the purchase, at least as many Millions of Fanta_USDs as there are players of the same role must remain available still to buy


#After purchasing a player, he must be removed from the list of real players to avoid buy it a second time

#At the same price, there are no criteria on which player to buy (the choice is free).

#If the budget for a role is not fully consumed, you can choose whether to add it to the budget for the role next or lose it (both solutions are fine)


def read_footballers(filename):
    try:
        players = []
        with open(filename) as file:
            for line in file:
                surname,team,role,price = line.strip().split(",")
                price = int(price)
                players.append([surname,team,role,price])
        
        return players
            
    except OSError as err:
        print(err)


def division(players):
    
    goalkeepers = []
    defenders = []
    midfielders = []
    forwards = []

    
    
    for player in players:
        role = player[2]
        
        if role == ' goalkeeper':
            goalkeepers.append(player)
            
        
        elif role == ' midfielder':
            defenders.append(player)
            

        elif role == ' midfielder':
            midfielders.append(player)
            

        elif role == ' forward':
            forwards.append(player)



    for k in range(100):
        for i in range(len(goalkeepers)):
            if i < len(goalkeepers)-1:
                if goalkeepers[i][-1] >= goalkeepers[i+1][-1]:
                    continue
                else:
                    goalkeepers[i][-1] ,goalkeepers[i+1][-1] = goalkeepers[i+1][-1],goalkeepers[i][-1]        
    
            elif i > 0:
                if goalkeepers[i-1][-1] >= goalkeepers[i][-1]:
                    continue
                else:
                    goalkeepers[i-1][-1] ,goalkeepers[i][-1] = goalkeepers[i][-1],goalkeepers[i-1][-1]        
    


    for k in range(100):
        for i in range(len(defenders)):
            if i < len(defenders)-1:
                if defenders[i][-1] >= defenders[i+1][-1]:
                    continue
                else:
                    defenders[i][-1] ,defenders[i+1][-1] = defenders[i+1][-1],defenders[i][-1]        
    
            elif i > 0:
                if defenders[i-1][-1] >= defenders[i][-1]:
                    continue
                else:
                    defenders[i-1][-1] ,defenders[i][-1] = defenders[i][-1],defenders[i-1][-1]
          



    
    for k in range(100):
        for i in range(len(midfielders)):
            if i < len(midfielders)-1:
                if midfielders[i][-1] >= midfielders[i+1][-1]:
                    continue
                else:
                    midfielders[i][-1] ,midfielders[i+1][-1] = midfielders[i+1][-1],midfielders[i][-1]        
    
            elif i > 0:
                if midfielders[i-1][-1] >= midfielders[i][-1]:
                    continue
                else:
                    midfielders[i-1][-1] ,midfielders[i][-1] = midfielders[i][-1],midfielders[i-1][-1]

    for k in range(100):
        for i in range(len(forwards)):
            if i < len(forwards)-1:
                if forwards[i][-1] >= forwards[i+1][-1]:
                    continue
                else:
                    forwards[i][-1] ,forwards[i+1][-1] = forwards[i+1][-1],forwards[i][-1]        
    
            elif i > 0:
                if forwards[i-1][-1] >= forwards[i][-1]:
                    continue
                else:
                    forwards[i-1][-1] ,forwards[i][-1] = forwards[i][-1],forwards[i-1][-1]  
      
    
    return goalkeepers,defenders,midfielders,forwards 


#W. 20 Millions  goalkeepers, 40 for defenders, 80 to midfielders and 120 to forwards

def puchaes(goalkeepers,defenders,midfielders,forwards):

    budget  =  20
    

    purchased_goalkeepers = []

    while True:
        for i in range(len(goalkeepers)):
            if goalkeepers[i][-1] > budget:
                continue
            elif goalkeepers[i][-1] <= budget:
                purchased_goalkeepers.append(goalkeepers[i])
                budget -= goalkeepers[i][-1]
            
        if budget == 0:
            break
    
    budget2  =  40

    purchased_defenders = []

    #while True:
     #   for i in range(len(defenders)):
      #      if defenders[i][-1] > budget2:
       #         continue
        #    elif defenders[i][-1] <= budget2:
         #       purchased_defenders.append(defenders[i])
          #      budget -= defenders[i][-1]
            
        #if budget2 == 0:
         #   break
    
    print(defenders)
    #print(purchased_defenders)
    


def main():
    players = read_footballers("fantafoot.txt")
    goalkeepers,defenders,midfielders,forwards = division(players)
    puchaes(goalkeepers,defenders,midfielders,forwards)


if __name__ == "__main__":
    main()