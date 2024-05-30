def ex3():
    # strat:stop:stop

    word = str(input("Enter a word:"))
    list1 = [word]
    list2 = []
    print("Let's play linked game, the first tow chracters that you enter should be as as 2 last characters of last word")
    print("The game is end when you neter a word that was spoken before")
    agree = str(input("if you agree,Enter 'YES' to play:"))
    if agree != "YES":
        pass
    else:
        while True:
            word1 = str(input("Enter a word:"))
            if word1 in list1 or word1 in list2:
                break
            else:
                if word1[0:2:] == list1[-1][-2::]:
                    list1.append(word1)
                    for i in range(len(list1)):
                        print(list1[i]," ",end = " ")
                    print()
                else:
                    list2.append(word1) 

ex3()  