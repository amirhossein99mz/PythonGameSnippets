def read_monudi_file(filename):
    try:
        with open(filename) as file:
            file1 = file.read().split("\n")
        
        numbers = []
        for line in file1:
            line = line.split()
            line = [int(i) for  i in line]
            numbers.append(line)
        
        return numbers
    
    except OSError as err:
        print(err)



def is_munodi_or_not(numbers):
    
    max_len = 0
    for i in range(len(numbers)):
        if len(numbers[i]) > max_len:
            max_len = len(numbers[i])
    list1 = []
    for i in range(len(numbers)):
        new = []
        len1 = len(numbers[i])
        if len1 != 1:
            if len1 != max_len:
                for j in range(len(numbers[i])):
                    a = None
                    if numbers[i][j] % 2 == 0:
                        if numbers[i][j+1] == (numbers[i][j])/2:
                            a = True
                            new.append(a)
                        else:
                            a = False
                            new.append(a)
                    elif numbers[i][j] % 2 != 0 and j<len(numbers[i])-1:
                        if numbers[i][j+1] == (3*(numbers[i][j]))+1:
                            a = True
                            new.append(a)
                        else:
                            a = False
                            new.append(a)
                list1.append(new)
            else:
                for j in range(len(numbers[i])):
                    a = None
                    if numbers[i][j] % 2 == 0:
                        if numbers[i][j+1] == (numbers[i][j])/2:
                            a = True
                            new.append(a)
                        else:
                            a = False
                            new.append(a)
                    elif numbers[i][j] % 2 != 0 and j<len(numbers[i])-1:
                        if numbers[i][j+1] == (3*(numbers[i][j]))+1:
                            a = True
                            new.append(a)
                        else:
                            a = False
                            new.append(a)
                list1.append(new)
        else:
            list1.append([True])      
    

   
    for i in range(len((list1))):
        if False not in list1[i] and len(list1[i])!= 1:
            print(f'Sequence {i+1} is a Munodi sequence (length {len(list1[i])+1})')
        elif  False not in list1[i] and len(list1[i])== 1:
            print(f'Sequence {i+1} is a Munodi sequence (length {len(list1[i])})')
        elif False in list1[i]:
            print(f'Sequence {i+1} is NOT a Munodi sequence')


def main():

    numbers = read_monudi_file("munodi_sequences.txt")
    result = is_munodi_or_not(numbers)
    
        

if __name__ == "__main__":
    main()