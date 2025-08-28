def read_characters_file(characters_file):
    try:
        matrix = []
        with open(characters_file) as file:
            file1 = file.read().split("\n")
            for line in file1:
                line = line.split(";")
                if line[0] == "Name":
                    continue
                else:
                    matrix.append(line)
        return(matrix)
    
    except OSError as err:
        print(err)



def read_questions_file1(questions_file1):

    try:
        matrix = []
        
        with open(questions_file1) as file:
            
            for line in file:
                question,answer = line.strip().split("=")
                question = question.strip()
                answer = answer.strip()
                matrix.append([question,answer])
        
        return(matrix)

    
    except FileNotFoundError as err:
        print(err)



def read_questions_file2(questions_file2):

    try:
        matrix = []
        
        with open(questions_file2) as file:
            
            for line in file:
                question,answer = line.strip().split("=")
                question = question.strip()
                answer = answer.strip()
                matrix.append([question,answer])
        
        return(matrix)

    
    except FileNotFoundError as err:
        print(err)


def process1(characters,question1):
    

    q11 = question1[0]
    result11 = []


    for line in characters:
        if q11[1] in line:
            result11.append(line)
    
    


    q12 = question1[1]
    result12 = []
    for line in result11:
        if q12[1] in line:
            result12.append(line)

    
    q13 = question1[2]
    result13 = []
    for line in result12:
        if q13[1] == line[4]:
            result13.append(line)
            
    return q11,result11,q12,result12,q13,result13



def process2(characters,question2):
    

    q21 = question2[0]
    result21 = []


    for line in characters:
        if q21[1] in line:
            result21.append(line)
    
    

    
    q22 = question2[1]
    result22 = []
    for line in result21:
        if q22[1] in line:
            result22.append(line)
    
    
    q23 = question2[2]
    result23 = []
    for line in result22:
        if q23[1] == line[-2]:
            result23.append(line)
   
    
    return q21,result21,q22,result22,q23,result23


def print_result1(q11,result11,q12,result12,q13,result13,characters):
    print()
    print("question 1")
    print()
    #Name;Gender;Hair color;Hair length;Glasses;Hat;Mustache;Beard;Bald
    Glasses = 4
    Hat = 5
    Mustache = 6 
    Beard = 7
    Bald = 8
    andis = {4:"Glasses",5:"Hat",6:"Mustache",7:"Beard",8:"Bald"}
    
    
    
    for i in range(len(characters)):
        for j in range(len(characters[i])):
            if characters[i][j] == "YES":
                if j in andis:
                    characters[i].append(andis[j])
                    
    print("Game characters:")
    for line in characters:
        header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
        if line[-1] == "NO":
            continue
        if line[-1] == "YES":
            continue
        else:
            header += " " 
            header += (line[-1])
        print(header)
    print()
    
    
    print(f"step 1-question: {q11[0]} = {q11[1]}")
    print("selected characterts:")
    for i in range(len(result11)):
        for j in range(len(result11[i])):
            if result11[i][j] == "YES":
                if j in andis:
                    result11[i].append(andis[j])
    

    for line in result11:

        header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
        if line[-1] == "NO" or line[-1] == "YES":
            print(header)
        else:
            header += " " 
            header += (line[-1])
            print(header)
    print()

    print(f"step 2-question: {q12[0]} = {q12[1]}")
    print("selected characterts:")
    
    print()
    
    for line in result12:

        header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
        if line[-1] == "NO" or line[-1] == "YES":
            print(header)
            
        else:
            header += " "
            header += (line[-1])
            print(header)
    print()

    
    print(f"step 3-question: {q13[0]} = {q13[1]}")
    print("selected characterts:")
    for i in range(len(result13)):
        for j in range(len(result13[i])):
            if result13[i][j] == "YES":
                if j in andis:
                    result13[i].append(andis[j])
    
   

    for line in result13:

        header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
        if line[-1] == "NO" or line[-1] == "YES":
            print(header)
            
        else:
            header += " " 
            header += (line[-1])
            print(header)
    print()
    print()
    if len(result13) == 1:
        print("Congratulations, you win! Character selected:")
        for line in result13:

            header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
            if line[-1] == "NO" or line[-1] ==  "YES":
                print(header)
            
            else:
                header += " "
                header += (line[-1])
                print(header)
        print()
        print()
        print()
    else:
        print("too bad,you lose.")

def print_result2(q21,result21,q22,result22,q23,result23,characters):

    #Name;Gender;Hair color;Hair length;Glasses;Hat;Mustache;Beard;Bald
    Glasses = 4
    Hat = 5
    Mustache = 6 
    Beard = 7
    Bald = 8
    andis = {4:"Glasses",5:"Hat",6:"Mustache",7:"Beard",8:"Bald"}
    
    
    
    for i in range(len(characters)):
        for j in range(len(characters[i])):
            if characters[i][j] == "YES":
                if j in andis:
                    characters[i].append(andis[j])
                    
    print("Game characters:")
    for line in characters:
        header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
        if line[-1] == "NO":
            continue
        if line[-1] == "YES":
            continue
        else:
            header += " " 
            header += (line[-1])
        print(header)
    print()
    
    
    print(f"step 1-question: {q21[0]} = {q21[1]}")
    print("selected characterts:")
    for i in range(len(result21)):
        for j in range(len(result21[i])):
            if result21[i][j] == "YES":
                if j in andis:
                    result21[i].append(andis[j])
    

    for line in result21:

        header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
        if line[-1] == "NO" or line[-1] == "YES":
            print(header)
        else:
            header += " " 
            header += (line[-1])
            print(header)
    print()

    print(f"step 2-question: {q22[0]} = {q22[1]}")
    print("selected characterts:")
    
    print()
    
    for line in result22:

        header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
        if line[-1] == "NO" or line[-1] == "YES":
            print(header)
            
        else:
            header += " "
            header += (line[-1])
            print(header)
    print()

    
    print(f"step 3-question: {q23[0]} = {q23[1]}")
    print("selected characterts:")
    for i in range(len(result23)):
        for j in range(len(result23[i])):
            if result23[i][j] == "YES":
                if j in andis:
                    result23[i].append(andis[j])
    
   

    for line in result23:

        header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
        if line[-1] == "NO" or line[-1] == "YES":
            print(header)
            
        else:
            header += " " 
            header += (line[-1])
            print(header)
    print()
    print()
    if len(result23) == 1:
        print("Congratulations, you win! Character selected:")
        for line in result23:

            header = (f"{line[0]} - Gender: {line[1]}, Hair color: {line[2]}, Hair length: {line[3]}")
            if line[-1] == "NO" or line[-1] ==  "YES":
                print(header)
            
            else:
                header += " "
                header += (line[-1])
                print(header)
        print()
        print()
        print()
    else:
        print("too bad,you lose.")
    

def main():

    characters = read_characters_file("characters.txt")
    question1 = read_questions_file1("question1.txt")
    question2 = read_questions_file2("question2.txt")
    q11,result11,q12,result12,q13,result13 = process1(characters,question1)
    q21,result21,q22,result22,q23,result23 = process2(characters,question2)
    print_result1(q11,result11,q12,result12,q13,result13,characters)
    print_result2(q21,result21,q22,result22,q23,result23,characters)
     
if __name__ == "__main__":
    main()

            