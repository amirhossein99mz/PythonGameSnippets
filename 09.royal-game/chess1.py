def read_players(file_name):
    try:
        players = {}
        with open(file_name) as file:
            for line in file:
                name,score = line.strip().split(",")
                if name == "PLAYER":
                    continue
                else:
                    players[name] = int(score)
        return players

    except OSError as err:
        print(err)



def read_games(file_name):
    try:
        games = []
        with open(file_name) as file:
            f = file.read().split("\n")
        for line in f:
            line = line.split(",")
            if line[0] == 'PLAYER A':
                pass
            else:
                games.append(line)
        
        return games
    
    except FileNotFoundError as err:
        print(err)

def delta(player_1, player_2): #(winner,loser)
    return 1/(1 + 2**((player_1 - player_2)/100))


def prcoess(players,games):


    for line in games:
        if line[0] not in players:
            players[line[0]] = 1500
        
        elif line[1] not in players:
            players[line[1]] = 1500

    for i in range(len(games)):
        if games[i][-1] ==  '1-0':
            score = round(200*delta(players[games[i][0]],players[games[i][1]]))
            players[games[i][0]] += score
            players[games[i][1]] -= score
        
        elif games[i][-1] ==  '0-1':
            score = round(200*delta(players[games[i][1]],players[games[i][0]]))
            players[games[i][0]] -= score
            players[games[i][1]] += score
 
        elif games[i][-1] == "1/2":
            pass
    
    return players

def print_result(players1):
    
    players = dict(sorted(players1.items(),key=lambda item:item[1],reverse=True))
    
    for key,value in players.items():
        
        print(f"{key} : {value}")

    
def main():
    players = read_players("players_short.csv")
    
    games = read_games("games_short.csv")

    players1 = prcoess(players,games)

    print_result(players1)

if __name__ == "__main__":
    main()