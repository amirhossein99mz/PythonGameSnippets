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
            
        
        elif role == ' defender':
            defenders.append(player)
            

        elif role == ' midfielder':
            midfielders.append(player)
            

        elif role == ' forward':
            forwards.append(player)


    return goalkeepers,defenders,midfielders,forwards

def puchaes(goalkeepers,defenders,midfielders,forwards):

    budget  =  20
    
    
    max = 0
    for i in range(len(goalkeepers)):
        if goalkeepers[i][-1] < budget:
            if goalkeepers[i][-1] > max:
                max = goalkeepers[i][-1]
                max1 = goalkeepers[i]
                index = i
                
    budget -= max
    
    purchased_goalkeepers = [max1]
    goalkeepers.pop(index)
    
    
    
    
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
    
    
    max = 0
    for i in range(len(defenders)):
        if defenders[i][-1] < budget2:
            if defenders[i][-1] > max:
                max = defenders[i][-1]
                max1 = defenders[i]
                index = i
                
    budget2 -= max
    
    purchased_defenders = [max1]
    defenders.pop(index)
    
    
    
    
    while True:
        for i in range(len(defenders)):
            if defenders[i][-1] > budget2:
                continue
            elif defenders[i][-1] <= budget2:
                purchased_defenders.append(defenders[i])
                budget2 -= defenders[i][-1]
            
        if budget2 == 0:
           break
    
    


    budget3  =  80
    
    
    max = 0
    for i in range(len(midfielders)):
        if midfielders[i][-1] < budget3:
            if midfielders[i][-1] > max:
                max = midfielders[i][-1]
                max5 = midfielders[i]
                index = i
                
    budget3 -= max
    
    purchased_midfielders = [max5]
    midfielders.pop(index)
    
    
    
    
    while True:
        for i in range(len(midfielders)):
            if midfielders[i][-1] > budget3:
                continue
            elif midfielders[i][-1] <= budget3:
                purchased_midfielders.append(midfielders[i])
                budget3 -= midfielders[i][-1]
            
        if budget3 == 0:
           break




    budget4  =  120
    
    
    max = 0
    for i in range(len(forwards)):
        if forwards[i][-1] < budget4:
            if forwards[i][-1] > max:
                max = forwards[i][-1]
                max1 = forwards[i]
                index = i
                
    budget4 -= max
    
    purchased_forwards = [max1]
    forwards.pop(index)

    max = 0
    for i in range(len(forwards)):
        if forwards[i][-1] < budget4:
            if forwards[i][-1] > max:
                max = forwards[i][-1]
                max2 = forwards[i]
                index = i
                
    budget4 -= max
    
    purchased_forwards = [max1,max2]
    forwards.pop(index)
    
    
    
    
    while True:
        for i in range(len(forwards)):
            if forwards[i][-1] > budget4:
                continue
            elif forwards[i][-1] <= budget4:
                purchased_forwards.append(forwards[i])
                budget4 -= forwards[i][-1]
            
        if budget4 == 0:
           break
    
    result = [purchased_goalkeepers,purchased_defenders,purchased_midfielders,purchased_forwards]

    return result

def main():
    players = read_footballers("fantafoot.txt")
    goalkeepers,defenders,midfielders,forwards = division(players)
    result = puchaes(goalkeepers,defenders,midfielders,forwards)

    list1 = result[0]
    list2 = result[1]
    list3 = result[2]
    list4 = result[3]
    
    print("Goalkeepers:",end=" ")
    for i in range(len(list1)):
        print(list1[i][0],list1[i][-1],end=" ")



    print()
    print()

    print("defenders:",end=" ")
    for i in range(len(list2)):
        print(list2[i][0],list2[i][-1],end=" ")



    print()
    print()
    
    print("midfielders:",end=" ")
    for i in range(len(list3)):
        print(list3[i][0],list3[i][-1],end=" ")  



    print()
    print()
    
    print("forwards:",end=" ")
    for i in range(len(list4)):
        print(list4[i][0],list4[i][-1],end=" ")  
    


if __name__ == "__main__":
    main()