def read_file(bowling_file):
    
    try:

        matrix = []
        list1 = []
        with open(bowling_file) as file:
            f = file.read().split("\n")
            for line in f:
                line = line.split(";")
                line[2:] = [int(i) for i in line[2:]]
                for el in line:
                    list1.append(el)
                matrix.append(list1)
                list1 = []
        
        sum_of_records = 0

        for line in matrix:
            for el in line[2:]:
                sum_of_records += el
            line.append(sum_of_records)
            sum_of_records = 0
        
        return(matrix)
       
    
    except OSError as err:
        print(err)
    

def process(bowling):
    
    for i in range(len(bowling)):
        
        if i < len(bowling)-1:
            
            if bowling[i][-1] > bowling[i+1][-1]:
                continue
            
            elif bowling[i][-1] < bowling[i+1][-1]:
                bowling[i][-1],bowling[i+1][-1] = bowling[i+1][-1],bowling[i][-1]
               
    name_max_10 = None
    surname_max_10 = None
    max_10 = 0
    name_max_0 = None
    surname_max_0 = None
    max_0 = 0
    
    for line in bowling:
        for el in line:
            if el == 10:
                max_10 += 1
            elif el == 0:
                max_0 += 1
        line.append(max_10)
        line.append(max_0)
        max_10 = 0
        max_0 = 0
    
    for line in bowling:
        
        if line[-1] > max_0 : 
            max_0 = line[-1]
            name_max_0 = line[0]
            surname_max_0 = line[1]
        
        if line[-2] > max_10 : 
            max_10 = line[-2]
            name_max_10 = line[0]
            surname_max_10 = line[1]
    
    for line in bowling:
        line.pop(-1)
        line.pop(-1)
    

    list2 = []
    bowling2 = []

    for line in bowling:
        list2.append(line[0])
        list2.append(line[1])
        list2.append(line[-1])
        bowling2.append(list2)
        list2 = []
    
    
    return bowling2,max_0,name_max_0,surname_max_0,max_10, name_max_10, surname_max_10

def prtnt_result(bowling2,max_0,name_max_0,surname_max_0,max_10, name_max_10, surname_max_10):
    
    for line in bowling2:
        for el in line:
            print(el,end=" ")
        print()
    
    print(f"Most 10 : {name_max_10} {surname_max_10} ({max_10} times)")
    print(f"Most 0 : {name_max_0} {surname_max_0} ({max_0} times)")


def main():

    bowling = read_file("bowling.txt")
    bowling2,max_0,name_max_0,surname_max_0,max_10, name_max_10, surname_max_10 = process(bowling)
    prtnt_result(bowling2,max_0,name_max_0,surname_max_0,max_10, name_max_10, surname_max_10)

if __name__ == "__main__":
    main()