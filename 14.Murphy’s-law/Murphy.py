def readMurphyLaw(murphyLaw):
    try:
        f = open(murphyLaw)
    except OSError as e:
        print(f"File does NOt exist, the main error is  {e}")
    
    matrix = []

    file = f.read().split("\n\n")
    
    for line in file:

        line = line.split("\n")
        lst = []
        for el in line:
            
            el = el.split()

            lst.append(el)
        matrix.append(lst)
    
    return(matrix)

    

def readArguements(arguements):
    try:
        f = open(arguements)
    except OSError as e:
        print(f"File does NOt exist, the main error is  {e}")
    
    matrix = []

    file = f.read().split("\n")
    
    return(file)

def findLaw(murphy,arguments):

    print(murphy)

    print()

    #print(arguments)

    result = []
    
    for line in murphy:
        for idx1 in arguments:
            for el in line:
                for idx in el:
                    if idx1 == idx:
                        result.append(line)

    
    for line in result:
        
        if len(line[1]) > 11:
            line[1] = line[1][0:12:1]
            line[1].append("...")
    
    for i in range(len(result)):
        result[i][0].append("-")
    print(result)

    for line in result:

        for el in line:

            for idx in el:

                print(idx,end=" ")
    print()
                        
                        
                     
                    


def main():
    
    murphy = readMurphyLaw("C:/Users/javan/OneDrive/Desktop/program/13.Done/Murphy_reads.txt")
    arguments =readArguements("C:/Users/javan/OneDrive/Desktop/program/13.Done/arguments.txt")
    findLaw(murphy,arguments)

if __name__ == "__main__":
    main()