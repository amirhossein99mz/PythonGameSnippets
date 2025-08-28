def readSkifile(filename):
    try:
        f = open(filename)
    except OSError as e:
        print(f"The error is {e}")

    file = f.read().split("\n")
    
    f.close()
    matrice = []
    
    TARGET_DATE = '2019-12-21'

    for line in file:
        line = line.split()
        

        if line[1] != TARGET_DATE:
            continue

        else:
            matrice.append(line)

    for line in matrice:
        line.pop(1)
        line[1] = int(line[1][0:2])
        line[2] = int(line[2][0:2])
    
    result = {}

    for line in matrice:
        result[line[0]] = {"start":line[1],"end":line[2],"type":None,"price":0}
    
    return(result)



def readPricefile(filename):
    try:
        f = open(filename)
    except OSError as e:
        print(f"The error is {e}")

    file = f.read().split("\n")
    
    f.close()

    matrice = []

    for line in file:
        line = line.split()
        line[-1] = int(line[-1])
        line[1] = line[1].split("-")
        matrice.append(line)

    print()
    

    matrices2 = []

    for line in matrice:
        line[1][0] = int(line[1][0][0:2])
        line[1][1] = int(line[1][1][0:2])
        a = line[1][0]
        b = line[1][1]
        c = line[-1]
        matrices2.append(line[0])
        matrices2.append(a)
        matrices2.append(b)
        matrices2.append(c)
    
    matrix = [matrices2[0:4],matrices2[4:8],matrices2[8:]]

    
    
    return(matrix)


def process(users,prices):
    
    print()
    
    resultn = {"Full":{0},"Morning":{0},"Afternoon":{0}}

    for line in prices:
        for key,value in users.items():
            if value['start'] > line[1] and value['end'] < line[2] and value['end']-value['start'] ==line[2]-line[1]-2 :
                value['type'] = line[0]
                value['price'] = line[-1]
                
    prices.pop(-1)

    
    for line in prices:
        for key,value in users.items():
            if value['start'] >= line[1] and value['end'] < line[2] :
                value['type'] = line[0]
                value['price'] = line[-1]
   


    
    count = 5
    total = 0
    for key,value in users.items():
         print(f"Skipass {key} : {value['type']} - {value['price']} EURO")
         total += value['price']
    
    
             
    print()
    print(f"total income : {float(total)}")
    print()
    
    
    
    
    

    count_mo = 0
    count_af = 0
    count_full = 0

    
    print("user status:")
    for key,value in users.items():
        if value['type'] == 'Full':
            count_full +=1
        elif value['type'] == 'Morning':
            count_mo += 1
        else:
            count_af += 1

    print(f"Full :{(count_full/count)*100} %")
    print(f"Morning: {(count_mo/count)*100} %")
    print(f"Afternoon: {(count_af/count)*100} %")

        
def main():
    
    users = readSkifile("users.txt")

    prices = readPricefile("prices.txt")

    process(users,prices)


if __name__ == "__main__":
    main()