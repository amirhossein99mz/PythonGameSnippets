def read_discographia(filename):
    try:
        with open(filename) as file:
            file1 = file.read().split()
        
        file2 = []
        for line in file1:
            line = line.split(";")
            file2.append(line)
        
        return file2
    
    except OSError as err:
        print(err)

def read_files(discography):
    
    files = discography
    filename = files[0][1] 
    for i in range(len(files)):
        filename = files[i][1]
        with open(filename) as file:
            for line in file:
                year,song = line.strip().split(";")
                year = int(year)
                files[i].append(year)
                files[i].append(song)
            
    
    for file in files:
        file.pop(1)
    
    songs = {}
    years = []

    for file in files:
        for el in file:
            if type(el) == int:
                years.append(el)
    


    #sorted(dict.items(),key=lambda itme:itme[0],reversed=True)
    
    for i in range(len(years)):

        if i > 0:
            if years[i] >= years[i-1]:
                pass
            elif years[i] < years[i-1]:
                years[i-1],years[i] = years[i],years[i-1]
        elif i < len(years)-1:
            if years[i+1] >= years[i]:
                continue
            elif years[i+1] < years[i]:
                years[i],years[i+1] = years[i+1],years[i]
    
    for year in years:
        songs[year] = None
    
    songs1 = list(sorted(songs.items(),key=lambda item:item[0]))
    songs = []
    for line in songs1:
        songs.append([line[0]])


    for i in range(len(files)):
        for line in songs:
            for j in range(len(files[i])):
                if line[0] == files[i][j]:
                    line.append([files[i][j+1],files[i][0]])
                    
    
    


    for i in range(len(songs)):
        print(songs[i][0],":")
        for j in range(len(songs[i])):
            if j > 0:
                for k in range(len(songs[i][j])):
                    if len(songs[i][j][0]) == 14:
                        a = (f"{songs[i][j][0]}                 {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 19:
                        a = (f"{songs[i][j][0]}            {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 25:
                        a = (f"{songs[i][j][0]}      {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 30:
                        a = (f"{songs[i][j][0]} {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 21:
                        a = (f"{songs[i][j][0]}          {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 20:
                        a = (f"{songs[i][j][0]}           {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 20:
                        a = (f"{songs[i][j][0]}           {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 18:
                        a = (f"{songs[i][j][0]}             {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 23:
                        a = (f"{songs[i][j][0]}            {songs[i][j][1]}  ")
                    elif len(songs[i][j][0]) == 13:
                        a = (f"{songs[i][j][0]}                  {songs[i][j][1]}  ")
                 
                
                print(a)
        
    
    print(years)


def main():
    discography = read_discographia("artists.txt")
    read_files(discography)



if __name__ == "__main__":
    main()