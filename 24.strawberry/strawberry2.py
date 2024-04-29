def read_strawberry(filename):
    try:
        words = []
        with open(filename) as file:
            file1 = file.read().split()
            for el in file1:
                if "..." not in el:
                    words.append(el)
                else:
                    el = el.strip("...")
                    words.append(el)
        return words
        
    except OSError as err:
        print(err)


def find_neighbours(strawberry):

    n = int(input("Enter a number (2 or 3): "))
    neighbours_3 = []
    neighbours_2 = []


    if n != 2 and n!= 3:
        print("worong number.")
    
    elif n == 3:
        for i in range(len(strawberry)):
            if i > 0 and i <= len(strawberry)-2:
                if len(strawberry[i-1]) == len(strawberry[i])  == len(strawberry[i+1]):
                    neighbours_3.append([strawberry[i-1],strawberry[i],strawberry[i+1]])

    else:
        for i in range(len(strawberry)):
            if  i < len(strawberry)-1:
                if   len(strawberry[i])  == len(strawberry[i+1]):
                    neighbours_2.append([strawberry[i],strawberry[i+1]])
    
    return n,neighbours_2,neighbours_3

    
def main():

    strawberry = read_strawberry("strawberry.txt")
    n,neighbours_2,neighbours_3 = find_neighbours(strawberry)
    
    if n == 3:
        for i in range(len(neighbours_3)):
            header = "("
            for j in range(len(neighbours_3[i])-1):
                header += "'"
                header += neighbours_3[i][j]
                header += "'"
                header += ","
            header += "'"
            header += neighbours_3[i][j]
            header += "'"
            header += ")"
            print(header)    
    
    else:
        for i in range(len(neighbours_2)):
            header = "("
            for j in range(len(neighbours_2[i])-1):
                header += "'"
                header += neighbours_2[i][j]
                header += "'"
                header += ","
            header += "'"
            header += neighbours_2[i][-1]
            header += "'"
            header += ")"
            print(header)

    
    #made by Amirmnz2024

if __name__ == "__main__":
    main()