def read_file(filename):
    try:
        with open(filename) as file:
            file2 = file.read().split("\n")
        worms = [line.split() for line in file2]
        
        return worms
    
    except OSError as err:
        print(err)

def process(worms):

    word1 = "line"
    word2 = "time"
  
    word11 = []
    word22 = []
    for i in range(len(worms)):
        new = [i]
        new2 = [i]
        for j in range(len(worms[i])):
            if worms[i][j] == word1:
                new.append(j)
            elif worms[i][j] == word2:
                new2.append(j)
        if len(new) > 1:
            word11.append(new)
        if len(new2) > 1:
            word22.append(new2)



    distance = 0
    word111 = []
    word222 = []
    for i in range(len(word11)):
        for j in range(len(word22)):
            if word11[i][0] != word22[j][0]:
                pass
            else:
                word111.append(word11[i])
                word222.append(word22[j])
    
  
    seq = []
    if len(word111)  == 0 or len(word222) == 0:
        print("The two words never appear in the same sequence")
    else:
        for i in range(len(word111)):
            for j in range(len(word222)):
                if word111[i][0] != word222[j][0]:
                    continue
                else:
                    if len(word111[i]) == len(word222[j]):
                        for k in range(len(word111[i])):
                            if k != 0:
                                distance = abs(word111[i][k]-word222[j][k])
                                seq.append([word111[i][0],distance])
                    else:
                        if len(word111[i]) > len(word222[j]):
                            len1 = len(word111[i])
                            len2 = len(word222[j])
                            new = [word111[i][0]]
                            for k in range(len(word222[j])):
                                if k != 0:
                                    distance = abs(word111[i][k]-word222[j][k])
                                    new.append(distance)
                                for t in range(len(word111[i][len2:len1+1])):
                                    if k != 0:
                                        distance =  abs(word111[i][len2:len1+1][t]-word222[j][k])
                                        new.append(distance)
                                    #print(word111[i][len2:len1+1][t])
                            seq.append(new)        
                                            

        min1 = 100
        seq2 = []
        for i in range(len(seq)):
            if len(seq[i]) == 2:
                seq2.append(seq[i])
            else:
                for j in range(len(seq[i])):
                    if j > 0:
                        if seq[i][j] < min1:
                            min1 = seq[i][j]
                seq2.append([i,min1])
    
        min2 = 100
        for i in range(len(seq2)):
            if seq2[i][1] < min2:
                min2 = seq2[i][1]
                index = i+1
    
        print(f"Min distance: sequence {index} (distance={min2})")

    
            
                         


def main():

    worms = read_file("worms.txt")
    process(worms)

if __name__ == "__main__":
    main()