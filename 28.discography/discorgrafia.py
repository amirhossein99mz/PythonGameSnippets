def read_artists_file(file_name):
    try:
        with open(file_name) as file:

            artists = []
            list1 = []
            for line in file:
                code,poet_file = line.strip().split(";")
                list1.append(code)
                list1.append(poet_file)
                artists.append(list1)
                list1 = []
                
        return(artists)
    
    except OSError as err:
        print(err)
    

def read_files(artists):
    
    try:
        
        list1 = []
        matrix = []
        for line in artists:
            
            code = line[0]
            
            with open(line[1]) as file:
                
                for line in file:
                    year,music = line.strip().split(";")
                    list1.append(code)
                    list1.append(year)
                    list1.append(music)
                    matrix.append(list1)
                    list1 = []
        
        return matrix
        
    except FileNotFoundError as err:
        print(err)


def comparison(songs):
    
    

    result = {}

    for line in songs:
        line[1] = int(line[1])
        result[line[1]] = []

    result2 = dict(sorted(result.items(),key=lambda item:item[0]))
    
        
    

    matrix1 = []
    list1 = []
    for key in result2:
        list1.append(key)
        matrix1.append(list1)
        list1 = []
    
    
    

    for i in range(len(songs)):
        for line in matrix1:
            if songs[i][1] == line[0]:
                line.append([songs[i][0],songs[i][-1]])

    return matrix1 
    

def print_result(result):
  
    print(result)
    for line in result:
        print(line[0])
        el = line[1:]
        for idx in el:
            print(f"{idx[1]} : {idx[0]}")
        print()
            
    

def main():

    artists = read_artists_file("artists.txt")
    songs = read_files(artists)
    result = comparison(songs)
    print_result(result)

if __name__ == "__main__":
    main()