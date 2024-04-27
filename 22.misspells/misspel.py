def read_names_file(filename):
    try:
        with open(filename) as file:
            names = file.read().split("\n")
        return names
    
    except OSError as err:
        print(err)

def read_parole_file(filename):
    try:
        with open(filename) as file:
            parole = file.read().split("\n")
        return parole
    
    except FileNotFoundError as err:
        print(err)

def comapre(word1,word2):

    word1 = word1.lower()
    word2 = word2.lower()

    differ = 0

    if len(word1) != len(word2):
        pass
    elif len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differ += 1
        
        if differ <= 1:
            return True
    return False


def find_words_almost_same(names,parole):
     
    final = []

    for i in range(len(names)):
        word1 = names[i]
        words = [word1]

        for j in range(len(parole)):
            word2 = parole[j]
            
            if comapre(word1,word2) == False:
                continue

            elif comapre(word1,word2) == True:
                words.append(word2)
        if len(words) >1:
            final.append(words)
        elif len(words) == 1:
            error = words
    
    final.append(error)

    return final


def main():

    names = read_names_file("names.txt")
    #Please, introduce the name of the file with the names:
    parole = read_parole_file("parole_italiane.txt")
    
    final= find_words_almost_same(names,parole)

    for i in range(len(final)):
        if len(final[i]) > 1:
            print(f"Name : {final[i][0]}")
            for j in range(len(final[i][1:])):
                print(final[i][1:][j])
            
            print()
        else:
            print(f"Name : {final[i][0]}")
            print("WARNING: No similar words were found!!!")
            
            print()
           


if __name__ == "__main__":
    main()