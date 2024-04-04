def read_products_file(file_name):
    try:
        pro = []
        with open(file_name) as file:
            for line in file:
                id,seller = line.strip().split()
                pro.append([id,seller])
        return pro
    except OSError as err:
        print(err)

def read_transactions_file(file_name):
    try:
        tra = []
        with open(file_name) as file:
            f = file.read().split("\n")
        for line in f:
            line = line.split()
            tra.append(line)
        
        return tra
    
    except FileNotFoundError as err:
        print(err)


def find_errros(pro,tra):

    errors = []

    for i in range(len(pro)):
        for j in range(len(tra)):
            if pro[i][0] == tra[j][0]:
               if pro[i][1] != tra[j][1]:
                   errors .append(tra[j])
    
    for i  in range(len(errors)):
        for j in  range(len(tra)):
            if errors[i][0] == tra[j][0]:
                if errors[i][1]!= tra[j][1]:
                    errors[i].append(tra[j][1])
    

    for k in range(len(pro)):
        for s in range(len(errors)):
            if pro[k][0]==errors[s][0]:
                errors[s].append(pro[k][1])
    
    return errors


def print_result(errors):
    
    print("Suspicous transactions ")
    print()
    for i in range(len(errors)):
        if len(errors[i]) > 3:
            print(f"Product code : {errors[i][0]}")
            print(f"Official seller : {errors[i][-1]}")
            print("Seller list:",end=" ")
            for el in errors[i][1:3]:
                print(el,end=" ")
            print()
        else:
            print(f"Product code : {errors[i][0]}")
            print(f"Official seller : {errors[i][-1]}")
            print(f"Seller list : {errors[i][1]}",end=" ")
        print()


def main():
    pro = read_products_file("products.txt")
    tra = read_transactions_file("transactions.txt")
    errors = find_errros(pro,tra)
    print_result(errors)

if __name__ == "__main__":
    main()