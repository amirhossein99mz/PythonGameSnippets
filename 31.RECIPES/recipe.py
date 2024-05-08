def read_food_file(file_name):
    try:
        result = {}
        with open(file_name) as file:
            for line in file:
                food,cost_per_kg,calory = line.strip().split(";")
                cost_per_kg = float(cost_per_kg)
                calory = int(calory)
                result[food] = {"cost":cost_per_kg,"calory":calory}
        
        return(result)
    
    except OSError as err:
        print(err)



def read_food2_file(file_name):
        
        try:
         
            with open(file_name) as file:
                file = file.read().split("\n")
            
            
            file = file[1:5]

            matrix = []
            for line in file:
                line = line.split(";")
                line[1] = int(line[1])
                matrix.append([line[0],line[1]])
        
            return(matrix)

        except OSError as err:
            print(err)

def calculate(foods,food1):
 
    print("ingerdient: ")
    for line in food1:
        print(f"{line[0]}  -  {line[1]:.1f}")
    print()
    print(f"number of ingredient: {len(food1)}")
    

    t_price = 0
    t_calory = 0
    for line in food1:
        if line[0] in foods:
            price = line[1]*foods[line[0]]['cost']
            calory = line[1]*foods[line[0]]['calory']
            t_calory += calory
            t_price += price
            price = 0
            calory = 0
    
    
    t_price = t_price/1000
    t_calory = t_calory/1000

    print(f"Recipe cost: {t_price}")
     
    print(f"Recipe calories{t_calory}")



def main():

    foods = read_food_file("foods.txt")
    
    food1 = read_food2_file("polenta_concia.txt")
    
    calculate(foods,food1)              

if __name__ == "__main__":
    main()