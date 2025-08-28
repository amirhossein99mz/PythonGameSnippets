def readQuotesFile(quotesFile):
    
    try:

        f = open(quotesFile)

    except OSError as e:
        
        print(f"The error is {e}")
    
    file = f.read().split("\n\n")
    
    f.close()

    matrix = []

    for line in file:

        line = line.split("\n")
        lst = []
        for el in line:
            el = el.split()
            lst.append(el)
        matrix.append(lst)
    return(matrix)

def readTopicsFile(topicesFile):
    
    try:

        f = open(topicesFile)

    except FileNotFoundError as e:
        
        print(f"The error is {e}")
    
    file = f.read().split("\n")

    f.close()

    return(file)

def findText(quotes,topics):

    print(quotes)
    print()
    print(topics)
    print()
    result = []
    
    
    for el in topics:

        for line in quotes:

            for idx in line:

                for idx1 in idx:

                    if el == idx1:

                        result.append(line)

    

    a = result[1]

    result[1] = result[2]
    
    result[2] = a

    #print(result)

    for line in result:

        if len(line) > 2:
        
            for el in line[2]:
                line[1].append(el)
            for el in line[3]:
                line[1].append(el)
            line.pop(-1)
            line.pop(-1)
    
    
    for line in result:

        if len(line[1]) > 10:
            line[1] = line[1][0:9]
            line[1].append("...")

    
    for line in result:

        line[0].append("-")

        for el in line:

            for idx in el:
                print(idx,end=" ")
        print() 


def main():

    quotes = readQuotesFile("C:/Users/javan/OneDrive/Desktop/program/14.Done/quotes.txt")

    topics = readTopicsFile("C:/Users/javan/OneDrive/Desktop/program/14.Done/topics.txt")
    
    findText(quotes,topics)
if __name__ == "__main__":
    main()