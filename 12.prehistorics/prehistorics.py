def readDeckFile(deckFile):
    
    try:
        f = open(deckFile)
    except OSError as e:
        print(f"The error is {e}")
    
    file = f.read().split("\n")
    f.close()
    
    cards = file
    card1 = []
    card2 = []

    player = 1

    for card in cards:
        if player == 1:
            card1.append(card)
            player = 2
        else:
            card2.append(card)
            player = 1
    
    return card1,card2

def Scores(score):

    scores = {"Red":5,"Green":3,"Yellow":1}

    if score in scores:
        return scores[score]
    else:
        return None

def main():

    card1,card2 = readDeckFile("C:/Users/javan/OneDrive/Desktop/program/15.Done/deckSmall.txt")
    
    table = []
    hand = 1
    score1 = 0
    score2 = 0
    
    print("Player 1's score:0")
    print("Player 2's score:0")
    print()

    while (len(card1)) > 0:
        
        card11 = card1.pop(0)
        card22 = card2.pop(0)

        table.append(card11)
        table.append(card22)

        if Scores(card11) > Scores(card22):
            winner = "Player 1"
            
            for card in table:
                score1 += Scores(card)
            table = [] 
        
        elif Scores(card11) < Scores(card22):
            winner = "Player 2"
            
            for card in table:
                score2 += Scores(card)
            table = [] 
        
        
        else :
            winner = None
            
        

        print(f"Hand{hand}:")
        print(f"player 1's card:{card11}")
        print(f"player 2's card:{card22}")
        if winner == None:
            print("result : draw")
        else:
            print(f"the {winner} wins the hand")
        print(f"player 1's point {score1}")
        print(f"player 1's point {score2}")

        hand += 1
        print()

    if score1 > score2:
        print(f"player 1 wins with {score1} point")
    
    elif score1 < score2:
        print(f"player 2 wins with {score2} point")
    else:
        print("match is draw")
    
main()