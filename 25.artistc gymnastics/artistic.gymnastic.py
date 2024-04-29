def read_socres(filename):
    try:
        with open(filename) as file:
            file1 = file.read().split("\n")
        
        scores = []
        for line in file1:
            line = line.split()
            scores.append(line)
        
        for i in range(len(scores)):
            for j in range(len(scores[i])):
                if j < 4 : 
                    pass 
                else:
                    scores[i][j] = float(scores[i][j])
        
        for i in range(len(scores)):
            for j in range(len(scores[i])):
                if j >= 4:
                    if j < len(scores[i])-1 :
                        if scores[i][j] > scores[i][j+1]:
                            scores[i][j],scores[i][j+1] = scores[i][j+1],scores[i][j]
                    if j >= 5:
                        if scores[i][j-1] > scores[i][j]:
                            scores[i][j-1],scores[i][j] = scores[i][j],scores[i][j-1]

        return scores
    except OSError as err:
        print(err)

def compute(scores):

    result = []
    
    count = 0

    for i in range(len(scores)):
        new = []
        for j in range(len(scores[i])-2):
            new.append(scores[i][j])
        result.append(new)
    
    

    for i in range(len(result)):
        count = 0
        for j in range(len(result)):
            if j >= 4:
                count += result[i][j]
        result[i].append(round(count,3))
    
    females = []

    for line in result:
        if line[2] == "F":
            females.append(line)
    
    max = 0
    for i in range(len(females)):
        if females[i][-1] > max:
            max = females[i][-1]
        
            females[i].append('max')
    
    for female in females:
        if female[-1] == 'max':
            print("Female winner:") 
            print(f"{female[0]} {female[1]}, {female[3]} - Score: {female[-2]}")

    
    nations = []

    for i in range(len(result)):
        if result[i][3] not in nations:
           nations.append(result[i][3])
    
    nations2 = []
    for el in nations:
        nations2.append([el,0])
    
    for line in result:
        for nation in nations2:
            if line[3] == nation[0]:
                if line[-1] != 'max':
                     nation[1] += line[-1]
                else:
                    nation[1] += line[-2]
    
   
    

    for i in range(len(nations2)):
        
        if i <= len(nations2[i])-2:
            if nations2[i][1] < nations2[i+1][1]:
                nations2[i],nations2[i+1] = nations2[i+1],nations2[i]
        
        if i >= 1 :
            if nations2[i-1][1] < nations2[i][1]:
                nations2[i-1],nations2[i] = nations2[i],nations2[i-1]
    

    
    nations2.pop(-1)
    
    print()
    print("Overall nations ranking:")

    for i in range(len(nations2)):

        if i == 0:
            print(nations2[i][0]," - ","Total score: ",nations2[i][1])
        else:
            print(f"{nations2[i][0]} - Final score : {nations2[i][1]}")



def main():

    scores = read_socres("scores.txt")
    
    compute(scores)

if __name__ == "__main__":
    main()