def read_text1_file(filename):
    try:
        with open(filename) as file:
            file1 = file.read().split("\n\n")
        
        text = []
        for i in range(len(file1)):
            new = []
            file1[i] = file1[i].split("\n")
            for j in range(len(file1[i])):
                if j == 0:
                    new.append([file1[i][j]])
                else:
                    file1[i][j] = file1[i][j].split()
                    for k in range(len(file1[i][j])):
                        new.append(file1[i][j][k])
                        new.append(" ")
                
            text.append(new)
        for line in text:
            line[1:] = [line[1:]]
        
        return text

    except OSError as err:
        print(err)

def read_topics1_file(filename):
    try:
        topics = []
        with open(filename) as file:
            for line in file:
                line = line.split("\n")
                topics.append(line[0])
        
        return topics

    except OSError as err:
        print(err)
    

def process(text,topics):
    #print(text)
    #print()
    #print(topics)
    #print()

    final = []

    for i in range(len(text)):
        for j in range(len(topics)):
            for k in range(len(text[i])):  
                if k == 0:
                    pass
                else:
                    if topics[j] in text[i][k]:
                        new = text[i]
        if new in final:
            pass
        else:
            final.append(new)
    
    return final

def print1_output(final):
    
    final2 = []

    for t in range(len(final)):
        new = []
        new.append(final[t][0])
        for s in range(len(final[t][1])):
            #print(final[t][1][s])
            if final[t][1][s] == " ":
                new.append(final[t][1][s])
            else:
                for j in range(len(final[t][1][s])):
                    new.append(final[t][1][s][j])
        final2.append(new)
   
    for line in final2:
        if len(line[1:]) <= 50:
            line[1:] = [line[1:]]
        else:
            line[1:] = [line[1:50]]
            line[1].append("...")
    


    for i in range(len(final2)):
        print(final2[i][0][0]," - ",end=" ")
        for j in range(len(final2[i][1])):
            print(final2[i][1][j],end="")
        print()
            




def main():

    text = read_text1_file("quotes.txt")

    topics = read_topics1_file("topics.txt")

    final = process(text,topics)
    
    print1_output(final)

if __name__ == "__main__":
    main()
    
                                        