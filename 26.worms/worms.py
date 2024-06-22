def read_worms1_file(filename):
    try:
        with open(filename) as file:
            file2 = file.read().split("\n\n")
        worms = []
        for line in file2:
            line = line.split("\n")
            for el in line:
                el = el.split()
                worms.append(el)
        
        return worms
    
    except OSError as err:
        print(err)

def find_min_daitance_worms2(worms):

    word1 = str(input("1.Enter a word:"))
    word2 = str(input("2.Enter a word:"))

    word11 = []
    word22 = []

    for i in range(len(worms)):
        new1 = [i]
        new2 = [i]
        for j in range(len(worms[i])):
            if worms[i][j] == word1:
                new1.append(j)
            elif worms[i][j] == word2:
                new2.append(j)
        if len(new1) > 1:
            word11.append(new1)
        
        if len(new2) > 1:
            word22.append(new2)

    word111 = []
    word222 = []
    for word_1 in word11:
        for word_2 in word22:
            if word_1[0] != word_2[0]:
                pass
            else:
                word111.append(word_1)
                word222.append(word_2)
    
    if len(word111) == len(word222) and len(word111) == 0:
        print("The two words never appear in the same sequence")
    else:
        distances = []
        for i in range(len(word111)):
            new = []
            for j in range(len(word222)):
                if word111[i][0] == word222[j][0]:
                    new.append(word111[i][0])
                    
                    if len(word111[i]) == len(word222[j]):
                        for k in range(len(word111[i])):
                            if k >= 1:
                                distance = abs(word111[i][k]-word222[j][k])
                                new.append(distance)
                    
                    elif len(word111[i]) > len(word222[j]):
                        len1 = len(word222[j])  
                        len2 = len(word111[i])+1 
                        for k in range(len(word222[j])):
                            if k >= 1:
                                distance = abs(word111[i][k]-word222[j][k])
                                new.append(distance)
                                    
                                for t in range(len(word111[i][len1:len2])):
                                    distance = abs(word111[i][len1:len2][t]-word222[j][k])
                                    new.append(distance)
                        
                    else:
                        len1 = len(word111[i]) 
                        len2 = len(word222[j])+1 
                        for k in range(len(word111[i])):
                            if k >= 1:
                                distance = abs(word111[i][k]-word222[j][k])
                                new.append(distance)
                                    
                                for t in range(len(word222[j][len1:len2])):
                                    distance = abs(word222[j][len1:len2][t]-word111[i][k])
                                    new.append(distance)
                    distances.append(new)
        
        min1 = 100
        distances2 = []
  
        for t in range(len(distances)):
            if len(distances[t]) == 2:
                distances2.append(distances[t])
            else:
                for s in range(len(distances[t])):
                    if s != 0:
                        if distances[t][s] < min1:
                            min1 = distances[t][s]
                            distances2.append([distances[t][0],min1])
        
        min2 = 100
        for m in range(len(distances2)):
            if distances2[m][1] < min2:
                min2 = distances2[m][1]
                index  = distances2[m][0]+1
        
        print(f"Min distance: sequence {index} (distance={min2})")


def main():
    
    worms = read_worms1_file("worms.txt")
    find_min_daitance_worms2(worms)
if __name__ == "__main__":
    main()