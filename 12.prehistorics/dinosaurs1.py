import random as r
def read_carts(filename):
    try:
        with open(filename) as file:
            cards = file.read().split("\n")
        return cards 
    except OSError as err:
        print(err)

def Scores(score):
    scores = {'Red':5,'Green':3,'Yellow':1}

    if score in scores:
        return scores[score]
    else:
        None     


def split(carts):
    
    player1 = []
    player2 = []
    player3 = []

    
    player = 1
    for i in range(len(carts)):
        if player == 1:
            player1.append(r.choice(carts))
            player = 2
        elif player == 2:
            player2.append(r.choice(carts))
            player = 3
        elif player == 3:
            player3.append(r.choice(carts))
            player = 1
       
    return player1,player2,player3


def main():

    carts = read_carts("deck.txt")
    player1,player2,player3 = split(carts)
    
    idx = 1
    table = []
    print("Player 1's score: 0")
    print("Player 2's score: 0")
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    while len(player1) > 0:
        cart1 = player1.pop(0)
        cart2 = player2.pop(0)
        cart3 = player3.pop(0)

        table.append(cart1)
        table.append(cart2)
        table.append(cart3)

        if Scores(cart1) > Scores(cart2)  and Scores(cart1) > Scores(cart3):
            winner = "PLAYER 1"
            for cart in table:
                score1 += Scores(cart)
            table = []
        
        elif Scores(cart2) > Scores(cart1)  and Scores(cart2) > Scores(cart3):
            winner = "PLAYER 2"
            for cart in table:
                score2 += Scores(cart)
            table = []
        
        if Scores(cart3) > Scores(cart2)  and Scores(cart3) > Scores(cart1):
            winner = "PLAYER 3"
            for cart in table:
                score3 += Scores(cart)
            table = []
        
        else:
            winner = None

        print()
        print("Hand",idx)
        print(f"Player 1's card :{cart1}")
        print(f"Player 2's card :{cart2}")
        print(f"Player 3's card :{cart3}")

        if winner == None:
            print("Result:draw")
        else:
            print(f"{winner} wins the hand.")
        
        print(f"Player 1's score:{score1}")
        print(f"Player 2's score:{score2}")
        print(f"Player 3's score:{score3}")

        idx += 1

    print()
    if score1 > score2 and score1 > score3:
        print(f"Player 1 wins with {score1} points.")
    
    elif score2 > score1 and score2 > score3:
        print(f"Player 2 wins with {score2} points.")
    
    elif score3 > score1 and score3 > score2:
        print(f"Player 3 wins with {score3} points.")
    
    else:
        print("Reuslt : draw")
        

if __name__ == "__main__":
    main()