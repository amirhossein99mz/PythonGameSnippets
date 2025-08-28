def read_ricette(filename):
    try:
        ricete = {}
        with open(filename) as file:
            for line in file:
                food,cost_per_kg,calories_per_kg = line.strip().split(";")
                cost_per_kg = float(cost_per_kg)
                calories_per_kg = int(calories_per_kg)
                ricete[food] = {"cost per 1 kg":cost_per_kg,"calories per 1 kg":calories_per_kg}
        
        return ricete
        
    except OSError as err:
        print(err)

def read_ricette2(filename):
    try:
        with open(filename) as file:
            file2 = file.read().split("\n")

        conica = []
        for line in file2[1:5]:
            line = line.split(";")
            line[1] = int(line[1])
            line[1] = line[1]/1000
            conica.append(line)
        
        return conica

    
    except OSError as err:
        print(err)

def main():

    ricette =  read_ricette("foods.txt")
    conica = read_ricette2("polenta_concia.txt")
    
   
    price = 0
    calories = 0
    for line in conica:
        if line[0] in ricette:
            price += (line[1]*ricette[line[0]]['cost per 1 kg'])
            calories += (line[1]*ricette[line[0]][ 'calories per 1 kg'])
    
    print("Ingredients")
    for line in conica:
        print(f"{line[0]} - {line[1]*1000}")
    print()
    print("Number of ingredient:",end=" ")
    print("Recipe cost:",round(price,2))
    print("Recipe calories:",calories)

if __name__ == "__main__":
    main()

    #f food, the cost per kg,  calories per kg, separated by a semicolon