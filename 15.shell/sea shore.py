def readPriceFile(price_file):
    try:
        f = open(price_file)
    except ValueError as e:
        print(f"The error is {e}")
    
    prices = {}
    
    file = f
    
    for line in file:
        shell,price = line.strip().split(":")
        prices[shell] = {"price":float(price),'num_choose':0,"offer":None}
    
    f.close()

    return(prices)

def readOfferFile(offers_file):

    try:
        f = open(offers_file)

    except FileNotFoundError as e:

        print(f"The second error is {e}")
    
    file = f.read().split("\n")

    f.close()

    matrice = []

    for line in file:
        line = line.split(":")
        if line[0] == line[0].split("-"):
            continue
        else:
            line[0] = line[0].split()
            matrice.append(line)
    
    for line in matrice:
        line[0].append(len(line[0]))

    result = {}

    for line in matrice:
        result[line[0][0]] = {"num_choose":line[0][-1],"offer":line[-1]}

    return result


def process(prices,offers):


    for key in offers:
        if key not in prices:
            continue
        else:
            prices[key]['num_choose'] = offers[key]['num_choose']
            prices[key]['offer'] = offers[key]['offer']
        
            
    return(prices)

def printCart(cart_file):
    try:
        f = open(cart_file)
    except ValueError as e:
        print(f"The Error is {e}")
    
    file = f.read().split("\n")
    
    f.close()
    
    matrice = []

    

    matrice = [file[0:3]+file[6:],[file[3],file[5]],[file[4]]]


    result = {}

    for line in matrice:
        result[line[0]] = len(line)

    return(result)


def conclude(price,cart):

    
    result = {}
    for key in cart:
        if key not in price:
            continue
        elif key in price:
            if cart[key] == price[key]["num_choose"]:
                a = key
                b = price[a]["num_choose"]
                c = price[a]["price"]
                d = price[a]["offer"]
                result[a] = {'number':b,'price':c,'offer':d,'total_price':b*c}
    
            elif cart[key] > price[key]["num_choose"]:
                a1 = key
                b1 = (price[a1]["num_choose"]+1)
                c1 = price[a1]["price"]
                d1 = price[a1]["offer"]
                result[a1] = {'number':b1,'price':c1,'offer':d1,'total_price':b1*c1}
    
    return(result)


def PrintResult(result):

    result1 = dict(sorted(result.items(),key = lambda item:item[1]['number']))
    
    
    matrice = []
    for key,value in result1.items():
        for i in range(2):
            row = []
            for i in range(value['number']):
                row.append(key)
            
            row.append(value['offer'])
            row.append(value['total_price'])
            row.append(value['number'])
        matrice.append(row)
    
    
    matrice[1][-2] = str(matrice[1][-2])
    matrice[1][-2] = (matrice[1][-2][0:5])
    matrice[1][-2] = float(matrice[1][-2][0:5])

    final_price = 0

    for line in matrice:
        print(f"As you buy ",end="")
        for el in line[0:line[-1]:1]:
            
            print(el,",",end=" ")
        print(";",end=" ")

        print(f"you got {line[2]} for free.")
        
        final_price += line[-2]
        
       
    print("Final price : %0.2f Euro" % final_price)  
    
       

            
            


    
def main():
    
    
    prices = readPriceFile("C:/Users/javan/OneDrive/Desktop/program/8.Done/prices.dat.txt")
    
    offers = readOfferFile("C:/Users/javan/OneDrive/Desktop/program/8.Done/offers.dat.txt")

    price = process(prices,offers)

    cart = printCart("C:/Users/javan/OneDrive/Desktop/program/8.Done/cart.dat.txt")

    result = conclude(price,cart)

    PrintResult(result)

if __name__ == "__main__":

    main()