def read_murphy_file(filename):
    try:
        
        with open(filename) as file:
            f = file.read().split("\n\n")
        murphy = []
        lst = []
        for line in f:
            line = line.split("\n")
            line0 = line[0]
            line1 = line[1:]
            for el in line1:
                el = el.split()
                for idx in el:
                    lst.append(idx)
            murphy.append([line0,lst])
            lst = []
        
        return murphy

    
    except OSError as err:
        print(err)

def read_arguments_file(filename):
    try:
        with open(filename) as file:
            words = file.read().split()
        return words        
    
    except OSError as err:
        print(err)    

                     

      

def main():

    murphy = read_murphy_file("Murphy_reads.txt")
    arguments = read_arguments_file("arguments.txt")
    
    result = []

    for argu in arguments:
        for line in murphy:
            for el in line[1]:
                if argu == el:
                    result.append(line)
    
    result.pop(0)

    for i in range(len(result)):
        title = result[i][0]
        text = result[i][1]
        text1 = text[0:20]
        print(title,"-",end="")
        for el in text1:
            print(el,end=" ")
        
        print()

    
        
    
    

if __name__ == "__main__":
    main()