#file1 = f.read().split() = [word,word,word,word]
#file2 = f.read().split("\n") = [line,line,line]
#file3=f.read().split("\n\n") = [line \n line \ n]

def read_word_sequence(file_name):
    try:

        with open(file_name) as f:
            file = f.read().split()
        new_words = []
        for word in file:
            normalized_word = word.strip("!?'.,:;").upper()
            new_words.append(normalized_word)
        return(new_words)
    

    except OSError as err:
        print(err)

def two_neighbours_same_length(words):
    
    for i in range(len(words)-1):
        if len(words[i]) == len(words[i+1]):
            print(f"('{words[i]}','{words[i+1]}')")


def three_neighbours_same_length(words):
     for i in range(len(words)-2):
        if len(words[i]) == len(words[i+1]) and len(words[i]) == len(words[i+2]):
            print(f"('{words[i]}','{words[i+1]}','{words[i+2]}')")
        

def main():

    words = read_word_sequence("text.txt")
    
    n = int(input("Enter 2 or 3:"))

    if n == 2:
        two_neighbours_same_length(words)
    elif n == 3:
        three_neighbours_same_length(words)
    
    else:
        print("NOT VALID")

if __name__ == "__main__":
    main()