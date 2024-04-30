def read_worms(filename):
    try:
        with open(filename) as file:
            file1 = file.read().split("\n")
        
        worms = []
        for line in file1:
            line = line.split()
            worms.append(line)
        
        return worms
       
    except OSError as err:
        print(err)


def find_short_distance(worms):

    worm1 = input("Enter a word : ")
    worm2 = input("Enter a word : ")
    


    worm1_1 = []
    worm2_2 = []


    for i in range(len(worms)):
        new = []
        for j in range(len(worms[i])):
            if worms[i][j] != worm1:
                pass
            elif worms[i][j] == worm1:
                new.append(i+1)
                new.append(j)
        if len(new) == 0:
            pass
        else:
            if len(new) == 6:
                worm1_1.append(new[0:2])
                worm1_1.append(new[2:])
                worm1_1.append(new[4:])
            elif len(new) == 4:
                worm1_1.append(new[0:2])
                worm1_1.append(new[2:])
            elif len(new) == 2:
                worm1_1.append(new)
    

    for i in range(len(worms)):
        new = []
        for j in range(len(worms[i])):
            if worms[i][j] != worm2:
                pass
            elif worms[i][j] == worm2:
                new.append(i+1)
                new.append(j)
        if len(new) == 0:
            pass
        else:
            if len(new) == 6:
                worm2_2.append(new[0:2])
                worm2_2.append(new[2:])
                worm2_2.append(new[4:])
            elif len(new) == 4:
                worm2_2.append(new[0:2])
                worm2_2.append(new[2:])
            elif len(new) == 2:
                worm2_2.append(new)
    
    
 
    if len(worm1_1) == 0 or len(worm2_2) == 0:
        print("The two words never appear in the same sequence")
    
    elif len(worm1_1) > 0 and  len(worm2_2) > 0:
        distances = []
        new = []
        for line in worm1_1:
            for el in worm2_2:
                if line[0] != el[0]:
                    continue
                elif line[0] == el[0]:   
                    new.append(line[0])
                    new.append(line[1])
                    new.append(el[1])
                distances.append(new)
                new = []
        
    
        if len(distances) == 0:
            print("The two words never appear in the same sequence")

        else:
            for i in range(len(distances)):
               distance = abs(distances[i][1]-distances[i][2])
               distances[i].append(distance)
    
        min = distances[0][-1]
        sequence = 0
        for i in range(len(distances)):
            if distances[i][-1] >= min:
                pass
            else:
                min = distances[i][-1]
                sequence = i
        if sequence != 0:
            print(f"Min distance: sequence {sequence} (distance = {min})")
     
                
    


 


def main():
    worms = read_worms("worms.txt")
    find_short_distance(worms)


if __name__ == "__main__":
    main()