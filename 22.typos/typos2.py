def openfile(filename):
    try:
        
        with open(filename) as file1:
            
            f = file1.read().split()
        
        return f
            
    except OSError as err:
        print(err)
        

def openfile1(filename1):
    try:

        with open(filename1) as file1:
            
            f = file1.read().split()
            
        return f 
            
    except OSError as err:
        print(err)
            
            
def comparison(word1,word2):
    
    word1=word1.lower()
    word2=word2.lower()
    
    differ = 0
    
    if len(word1)!= len(word2):
        return False
    
    elif len(word1)==len(word2):
        
        for i in range(len(word1)):
            
            if word1[i]==word2[i]:
                continue
            
            elif word1[i]!=word2[i]:
                differ+=1
    
    if differ <= 1:
        
        return True
     
    return False
            
            
def main():
    
    names = openfile("names.txt")
    words = openfile1("parole_italiane.txt")
    
    final=[]
    
    for i in range(len(names)):
        word1=names[i]
        first=[word1]

        for j in range(len(words)):
            word2=words[j]
            if comparison(word1,word2):
                first.append(word2)
        if len(first)>1:
            final.append(first)
            first = []
    

    for i in range(len(final)):
            print(f"Name: {final[i][0]}")
            for j in range(1,len(final[i])):
                print(final[i][j])
                

if __name__=='__main__':
    main()