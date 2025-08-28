def read_glucomter_file(file_name):
    try:

        matrix = []

        with open(file_name) as file:
            for line in file:
                id,time,index,temp,bpm = line.strip().split()
                index = int(index)

                if index < 200:
                    pass
                else:
                    matrix.append([id,time,index]) 
        
        for i in range(len(matrix)):
            if i > 0:
                if matrix[i-1][-1] > matrix[i][-1]:
                    matrix[i-1][-1],matrix[i][-1] = matrix[i][-1],matrix[i-1][-1]
        
       
        return matrix

    except OSError as err:
        print(err)

def main():

    glucometer = read_glucomter_file("glucometer.txt")
    
    for i in range(len(glucometer)):
        print(" ".join(str(x) for x in glucometer[i]))


if __name__ == "__main__":
    main()