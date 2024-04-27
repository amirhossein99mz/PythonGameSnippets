def compare_words(word1,word2):
    
    differ = 0
    

    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) != len(word2):
        pass
    elif len(word1) == len(word2):
        
        for i in range(len(word1)):
            
            if word1[i] == word2[i]:
                continue
            elif word1[i] != word2[i]:
                differ += 1
        
        if differ == 1:
            return True
    return False

def main():
    word1 = input("Enter word1:")
    word2 = input("Enter word1:")

    if compare_words(word1,word2):
        print("YES")
    else:
        print("NO")

main()