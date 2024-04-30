def read_worm_file(file_name):
    try:
        
        with open(file_name) as f:
            file = f.read().split("\n")
        matrice = []
        for line in file:
            line = line.split()
            matrice.append(line)
        return matrice
    
    except OSError as err:
        print(err)
    

def find_min_distance(sequences):

    result1 = {}
    result2 = {}

    min_distance = 0
    for line in sequences:
        if len(line) > min_distance:
            min_distance = len(line)
    
    
    word1 = input("Enter first word:")
    word2 = input("Enter second word:")
    
    
    min_distance_index = 0

    for row in range(len(sequences)):
        for col in range(len(sequences[row])):
            if sequences[row][col] == word1:
                index1 = row
                index2 = col
            
                if index1 in result1:
                    result1[index1].append(index2)
                else:
                    result1[index1] = [index2]
    

    for row in range(len(sequences)):
        for col in range(len(sequences[row])):
            if sequences[row][col] == word2:
                index1 = row
                index2 = col
            
                if index1 in result2:
                    result2[index1].append(index2)
                else:
                    result2[index1] = [index2]
    
    for key in result2:
        if key in result1:
            for el in result1[key]:
                for idx in result2[key]:
                    distance = abs(el-idx)
                    if distance < min_distance:
                        min_distance = distance
                        min_distance_index = key+1
    
    result= [min_distance_index,min_distance]
    
    return result


def print_result(result):

    if result[0] == 0:
        print("The two words never appear in the same sequence")
    else:
        print(f"Min distance: sequence {result[0]} (distance={result[1]})")



def main():

    sequences = read_worm_file("worms.txt")
    result = find_min_distance(sequences)
    print_result(result)   
if __name__ == "__main__":
    main()
