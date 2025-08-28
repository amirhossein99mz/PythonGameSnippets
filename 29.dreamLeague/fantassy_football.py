def read_file(file_name):
    try:

        players = {}
        
        with open(file_name) as file:
            for line in file:
                surname,team,position,price = line.strip().split(",")
                price = int(price)
                players[surname] = {"pos":position,"price":price}
        
        return(players)

    except OSError as err:
        print(err)


def purcahes_goalkeepers(players):

    
    goalkeepers = [] #20$ len:3
    
    
    budget_g = 20
    
    while budget_g > 0:
        for key,value in players.items():
            if value["pos"] == ' goalkeeper' and value['price'] <= budget_g:
                goalkeepers.append([key,value['price']])
                budget_g -= value['price']
        if budget_g == 0:
            break
    
    if len(goalkeepers) > 3:
        goalkeepers = goalkeepers[0:3:1]
             
  
    return goalkeepers



def purcahes_defenders(players):

    defenders   = [] #40$ len:8

    budget_def= 40
    while budget_def > 0:
        for key,value in players.items():
            if value["pos"] == ' defender' and value['price'] <= budget_def:
                defenders.append([key,value['price']])
                budget_def -= value['price']
        if budget_def == 0:
            break
    
    if len(defenders) > 8:
        defenders = defenders[0:8:1]
    
    return defenders



def purcahes_midfielders(players):

    midfielders = [] #80$ len:8

    budget_mi = 80
    while budget_mi > 0:
        for key,value in players.items():
            if value["pos"] == ' midfielder' and value['price'] <= budget_mi:
                midfielders.append([key,value['price']])
                budget_mi -= value['price']
        if budget_mi == 0:
            break
    
    if len(midfielders) > 8:
        midfielders = midfielders[0:8:1]
    
    return midfielders


def purcahes_forwards(players):   
    
    forwards  = [] #120$ len:6
    
    budget_fo = 120
    while budget_fo > 0:
        for key,value in players.items():
            if value["pos"] == ' midfielder' and value['price'] <= budget_fo:
                forwards.append([key,value['price']])
                budget_fo -= value['price']
        if budget_fo == 0:
            break
    
    if len(forwards) > 8:
        forwards = forwards[0:6:1]
    
    return forwards




def main():

    players = read_file("fantafoot.txt")
    

    go = purcahes_goalkeepers(players)
    de = purcahes_defenders(players)
    mi = purcahes_midfielders(players)
    fo = purcahes_forwards(players)

    print("Goalkeepers: ",end=" ")
    for line in go:
        print(f"{line[0]} {line[1]}"," ",end=" ")
    print()
    print()


    print("defenders: ",end=" ")
    for line in de:
        print(f"{line[0]} {line[1]}"," ",end=" ")
    print()
    print()


    print("midfielders: ",end=" ")
    for line in mi:
        print(f"{line[0]} {line[1]}"," ",end=" ")
    print()
    print()


    print("forwards: ",end=" ")
    for line in fo:
        print(f"{line[0]} {line[1]}"," ",end=" ")
    print()
    print()

    
    

if __name__ == "__main__":
    main()