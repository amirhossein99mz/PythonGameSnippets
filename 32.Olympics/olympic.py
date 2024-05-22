def read_file(filename):
    try:
        with open(filename) as file1:
            
            file = file1.read().split("\n")
        
        matrix = []
        for line in file:
            line = line.split("-")
            matrix.append(line)
        
        return matrix
    
    except FileNotFoundError as err:
        print(err)
    
def process(matrix):
    
    for i in range(len(matrix)):
        
        matrix[i][3] = matrix[i][3].split(",")
        matrix[i][3][-1] = int(matrix[i][3][-1])
        matrix[i][3][0] = matrix[i][3][0].split()
        matrix[i][3][0][1] = int(matrix[i][3][0][1])
        matrix[i][3] = [matrix[i][3][0][0],matrix[i][3][0][1],matrix[i][3][-1]]
        
        matrix[i][-1] = matrix[i][-1].split(",")
        matrix[i][-1][-1] = matrix[i][-1][-1].split()
        matrix[i][-1][-1].pop(-1)
        matrix[i][-1].append(matrix[i][-1][-1][0])
        matrix[i][-1].pop(-2)
        matrix[i][-1] = [int(i) for i in matrix[i][-1]]

    
    return matrix


def categorize_athletes(players):
    
    field1 = []
    nation1 = []
    medal1 = []
    for i in range(len(players)):
        new = []
        players[i][1] = players[i][1].strip()
        players[i][2] = players[i][2].strip()
        players[i][4] = players[i][4].strip()
        
        field = players[i][1]
        medal = players[i][2]
        nation = players[i][4]
        
        new.append(nation)
        if new not in nation1:
            nation1.append(new)
        new = []

        new.append(field)
        if new  in field1:
            continue
        else:
            field1.append(new)
        new = []

        
        new.append(medal)
        if new  in medal1:
            continue
        else:
            medal1.append(new)
        new = []
        
    
    for i in range(len(players)):
        for line in nation1:
            if players[i][4] == line[0]:
                if players[i] not in line:
                    line.append([players[i]])


    for i in range(len(players)):
        for line in field1:
            if players[i][1] == line[0]:
                if players[i] not in line:
                    line.append([players[i]])
    
   
    for i in range(len(players)):
        for line in medal1:
            if players[i][2] == line[0]:
                if players[i] not in line:
                    line.append([players[i]])
    
    return field1,nation1 ,medal1

def print1_result(field1,nation1 ,medal1):
    
    for i in range(len(field1)):
        print("The filed:",field1[i][0])
        field1[i].pop(0)
        print("name:",field1[i][0][0][0])
        print("medal:",field1[i][0][0][2])
        print("Date of birth:",end=" ")
        header = f"{field1[i][0][0][3][0]}"
        header += ","
        header += f"{field1[i][0][0][3][1]}"
        header += ","
        header += f"{field1[i][0][0][3][2]}"
        print(header)
        print("nationality:",field1[i][0][0][4])
        if len(field1[i][0][0][5]) == 1:
            print(f"The athlete won the olympics games in the year :{field1[i][0][0][5][0]} ")
        else:
            header1 = ("The athlete won the olympics games in the years:")
            for j in range(len(field1[i][0][0][5])-1):
                header1 += (f"{field1[i][0][0][5][j]}")
                header1 += ","
            header1 += (f"{field1[i][0][0][5][-1]}")
            print(header1)
        print()
        print()
    

    print()
    
    print()

    for i in range(len(nation1)):
        print("nationality:",nation1[i][0])
        nation1[i].pop(0)
        print("name:",nation1[i][0][0][0])
        print("field:",nation1[i][0][0][1])
        print("medal:",nation1[i][0][0][2])
        print("Date of birth:",end=" ")
        header = f"{nation1[i][0][0][3][0]}"
        header += ","
        header += f"{nation1[i][0][0][3][1]}"
        header += ","
        header += f"{nation1[i][0][0][3][2]}"
        print(header)
        #print("nationality:",nation1[i][0][0][4])
        if len(nation1[i][0][0][5]) == 1:
            print(f"The athlete won the olympics games in the year :{nation1[i][0][0][5][0]} ")
        else:
            header1 = ("The athlete won the olympics games in the years:")
            for j in range(len(nation1[i][0][0][5])-1):
                header1 += (f"{nation1[i][0][0][5][j]}")
                header1 += ","
            header1 += (f"{nation1[i][0][0][5][-1]}")
            print(header1)
        print()
        print()
    

    for i in range(len(medal1)):
        print("medal:",medal1[i][0])
        medal1[i].pop(0)
        print("name:",medal1[i][0][0][0])
        print("field:",medal1[i][0][0][1])
        #print("medal:",nation1[i][0][0][2])
        print("Date of birth:",end=" ")
        header = f"{medal1[i][0][0][3][0]}"
        header += ","
        header += f"{medal1[i][0][0][3][1]}"
        header += ","
        header += f"{medal1[i][0][0][3][2]}"
        print(header)
        print("nationality:",medal1[i][0][0][4])
        if len(medal1[i][0][0][5]) == 1:
            print(f"The athlete won the olympics games in the year :{medal1[i][0][0][5][0]} ")
        else:
            header1 = ("The athlete won the olympics games in the years:")
            for j in range(len(medal1[i][0][0][5])-1):
                header1 += (f"{medal1[i][0][0][5][j]}")
                header1 += ","
            header1 += (f"{medal1[i][0][0][5][-1]}")
            print(header1)
        print()
        print()
    
    
          
 
def main():
    
    matrix = read_file("olympic.txt")
    
    players = process(matrix)

    field1,nation1 ,medal1 = categorize_athletes(players)

    print1_result(field1,nation1 ,medal1)


    
if __name__ == "__main__":
    main()