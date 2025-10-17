def read_prices(filename):
    try:
        prices = []
        with open(filename) as file:
            f = file.read().split("\n")
        
        for line in f:
            line = line.split(":")
            line[1] =float(line[1])
            prices.append([line[0],line[1]])
        
        return prices
            
    except OSError as err:
        print(err)




def read_offers(filename):
    try:
        list1 = []
        offers = []
        with open(filename) as file:
            for line in file:
                line = line.split(":")
                line[0] = line[0].split()
                line[1]=line[1].split("\n")
                for el in line[0]:
                    list1.append(el)
                list1.append(line[1][0])
                offers.append(list1)
                list1 = []
        
        return offers
        
    
    except FileNotFoundError as err:
        print(err)




def read_carts(filename):
    try:
        with open(filename) as file:
            carts = file.read().split("\n")
        
        return carts
    
    except ValueError as err:
        print(err)


def combine_two_files(prices,offers):


    pirces_and_offers = {}

    for line in prices:
        for el in offers:
            if line[0] == el[0]:
                pirces_and_offers[line[0]] = {"price":line[1],"if you choose":(len(el)-1),"offer":el[-1]}
            
    return pirces_and_offers


def process(carts,pirces_and_offers):

    
    cartss = []

    count_cart = 0
    cart1 = carts[0]
    for cart in carts:
        if cart == cart1:
            count_cart += 1
    
    cartss.append([cart1,count_cart])
    
    

    
    count_cart = 0
    cart2 = [i for i in carts if i!=cart1]
    cart2 = cart2[0]
    for cart in carts:
        if cart == cart2:
            count_cart += 1
    
    cartss.append([cart2,count_cart])
    
    

    
    count_cart = 0
    cart3 = [i for i in carts if i!=cart2]
    cart3 = cart3[0]
    for cart in carts:
        if cart == cart3:
            count_cart += 1
    
    cartss.append([cart3,count_cart])
     
    result = {}

    for cart in cartss:
        if cart[0] not in pirces_and_offers:
            continue
        else:
            if cart[1] == pirces_and_offers[cart[0]][ 'if you choose']:
                result[cart[0]] = {"price":cart[1]*pirces_and_offers[cart[0]]['price'],'offer':pirces_and_offers[cart[0]]['offer'],"number":cart[1]}

            else:
                result[cart[0]] = {"price":round((cart[1]-1)*pirces_and_offers[cart[0]]['price'],2),'offer':pirces_and_offers[cart[0]]['offer'],"number":pirces_and_offers[cart[0]][ 'if you choose']}
    
    return result
    


def print_result(result):
   
    
    total_price = 0
    carts = []
    for key,value in result.items():
        total_price += value['price']
        carts.append([key,value[ 'offer'],value[ 'number']])
    
    total_price = round(total_price,2)

    headers= []
    
    for cart in carts:
        header = 'As you buy '
        for i in range(cart[-1]):
            header += cart[0]
            header += ", "
        header += ";"
        header += "you got "
        header += cart[1]
        header += " for free"
        headers.append(header)
        header = None
    
    for header in headers:
        print(header)

    print(f"Final price: {total_price} EUR")

def main():

    prices = read_prices("prices.dat.txt")
    offers = read_offers("offers.dat.txt")
    carts = read_carts("cart.dat.txt")
    pirces_and_offers = combine_two_files(prices,offers)
    result = process(carts,pirces_and_offers)
    print_result(result)

if __name__ == "__main__":
    main()
