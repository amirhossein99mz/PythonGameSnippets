def read_names_file(names_file):

    try:
        with open(names_file) as f:
            file = f.read().split()
            #file = [line.strip() for line in f]
            #file= f.read().split("\n\n")
        return file

    except OSError as err:
        print(err)



def read_words_file(words_file):

    try:
        with open(words_file) as f:
            
            file = f.read().split("\n")
        return file

    except FileNotFoundError as err:
        print(err)

def comaprison(word1,word2):

    word1 = word1.lower()
    word2 = word2.lower()

    differ = 0

    if len(word1) != len(word2):
        return False
    
    elif len(word1) == len(word2):

        for i in range(len(word1)):

            if word1[i] == word2[i]:
                continue
            elif word1[i] != word2[i]:
                differ += 1
    
    if differ <= 1:
        return True
    return False

def find_result(names,words):

    result = []
    
    for i in range(len(names)):
        word1 = names[i]
        final = [word1]
        
        for j in range(len(words)):
            word2 = words[j]
            
            if comaprison(word1,word2)==True:
                final.append(word2)
        
        if len(final) >1:
            result.append(final)
    
    return(result)

def print_result(result):
    
    for i in range(len(result)):
        print(f"name :{result[i][0]}")
        print(f"same words:")
        for j in range(len(result[i][1:])):
            print(f"{result[i][j]}")



def main():
    
    names = read_names_file("names.txt")
    words = read_words_file("parole_italiane.txt")
    result = find_result(names,words)
    print_result(result)
    

if __name__ == "__main__":
    main()