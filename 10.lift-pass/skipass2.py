def read_users_file(filename):
    try:
        users = []
        
        with open(filename) as file:
            for line in file:
                id,target_date,start,stop = line.strip().split()
                if target_date != "2019-12-21":
                    continue
                else:
                    if start[0] == "0":
                        start1 = start[1:2]
                    else:
                        start1 = start[0:2]
                    if stop[0] == "0":
                        stop1 = stop[1:2]
                    else:
                        stop1 = stop[0:2]
                    
                    users.append([id,target_date,int(start1),int(stop1)])
        
        return users
                    
    except OSError as err:
        print(err)


def read_prices_file(filename):
    try:
        prices = []
        
        with open(filename) as file:
            f = file.read().split("\n")
        
        for line in f:
            line = line.split()
            time = line[0]
            price = int(line[-1])
            line[1] = line[1].split("-")
            
            for i in range(len(line[1])):
                if line[1][0] == "0":
                    start = int(line[1][0][1:2])
                elif line[1][0] != "0":
                    start = int(line[1][0][0:2])

                end = int(line[1][1][0:2])
            
            prices.append([time,start,end,price])
    
        return prices
        
        
    except FileNotFoundError as err:
        print(err)

def calculate_price(users,prices):

   
    
    result = []

    for i in range(len(prices)):
        for j in range(len(users)):
            if prices[i][1] == (users[j][-2])-1 and prices[i][2] == (users[j][-1])+1:
                users[j].append(prices[i][0])
                users[j].append(prices[i][-1])
            
    for i in range(len(users)):
        if len(users[i]) >4:
            result.append(users[i])
            index = i
    
    users.pop(index)
    prices.pop(-1)




    for el in users:
        for line in prices:
            if el[2] >= line[1] and el[3] <= line[-2]:
                el.append(line[0])
                el.append(line[-1])
    
    
    
    for line in users:
        result.append(line)
    
    return result
   
def print_result(skipass):
    
    
    morning = 0
    afternoon = 0
    full = 0
    total = len(skipass)


    total_income  = 0
    for ski in skipass:
        print(f"Skipass {ski[0]}: {ski[-2]} - {ski[-1]} EURO")
        total_income += ski[-1]
        
        if ski[-2] == 'Afternoon':
            afternoon  += 1
        
        elif ski[-2] == 'Morning':
            morning  += 1

        elif ski[-2] == 'Full':
            full += 1
        
    print()
    print(f"Total income: {total_income:.2f}")  
    print()

    print("User status:")
    print(f"Morning {(morning/total)*100} %")
    print(f"Afternoon {(afternoon/total)*100} %")
    print(f"Full {(full/total)*100} %")




def main():

    users = read_users_file("users.txt")
    prices = read_prices_file("prices.txt")
    skipass = calculate_price(users,prices)
    print_result(skipass)

    
    

if __name__ == "__main__":
    main()