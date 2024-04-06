def read_students_file(file_name):
    try:
        matrix = []
        with open(file_name) as file:
            f =  file.read().split("\n")
            for line in f:
                line = line.split()
                matrix.append(line)



        for i in range(len(matrix)):
            if i == 0:
                for j in range(len(matrix[i])):
                    com = matrix[i][0]
                    math = matrix[i][1]
                    geo = matrix[i][2]
        matrix.pop(0)
        
        
        students = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                students[matrix[i][0]] = {com:matrix[i][1],math:matrix[i][2],geo:matrix[i][3]}
        
        
        for key,value in students.items():
            if value['computerScience'] == "30L":
                value['computerScience'] = 33
            else:
                value['computerScience'] = int(value['computerScience'])
            
            if value[ 'MathematicalAnlysis1'] == "30L":
                value[ 'MathematicalAnlysis1'] = 33
            else:
                value[ 'MathematicalAnlysis1'] = int(value[ 'MathematicalAnlysis1'])

            if value[ 'Geometry'] == "30L":
                value[ 'Geometry'] = 33
            else:
                value[ 'Geometry'] = int(value[ 'Geometry'])
         

        return students

    except OSError as err:
        print(err)



def process_computer_science(students):
    
    sum_of_grades = 0
    number_of_students = 0
    number_of_passed = 0
    best_score = 0
    best_score_stuednt_id = None
   
    for key,value in students.items():
        sum_of_grades += value['computerScience']
        number_of_students += 1
        if value['computerScience'] >= 18:
            number_of_passed += 1
        if value['computerScience'] >= best_score:
            best_score = value['computerScience']
            best_score_stuednt_id = key
        
    average_score = sum_of_grades/number_of_students

    computer_science = [average_score,best_score,best_score_stuednt_id,number_of_passed]
    
    return computer_science


def process_mathematical_anlysis1(students):
    
    sum_of_grades = 0
    number_of_students = 0
    number_of_passed = 0
    best_score = 0
    best_score_stuednt_id = None
   
    for key,value in students.items():
        sum_of_grades += value[ 'MathematicalAnlysis1']
        number_of_students += 1
        if value[ 'MathematicalAnlysis1'] >= 18:
            number_of_passed += 1
        if value[ 'MathematicalAnlysis1'] >= best_score:
            best_score = value[ 'MathematicalAnlysis1']
            best_score_stuednt_id = key
        
    average_score = sum_of_grades/number_of_students

    mathematical_anlysis1 = [average_score,best_score,best_score_stuednt_id,number_of_passed]
    
    return mathematical_anlysis1


def process_geometry(students):
    
    sum_of_grades = 0
    number_of_students = 0
    number_of_passed = 0
    best_score = 0
    best_score_stuednt_id = None
   
    for key,value in students.items():
        sum_of_grades += value[ 'Geometry']
        number_of_students += 1
        if value[ 'Geometry'] >= 18:
            number_of_passed += 1
        if value[ 'Geometry'] >= best_score:
            best_score = value[ 'Geometry']
            best_score_stuednt_id = key
        
    average_score = sum_of_grades/number_of_students

    geometry = [average_score,best_score,best_score_stuednt_id,number_of_passed]
   
    return  geometry

def print_results(computer_science,mathematical_anlysis1,geometry):

    print("computer science:")

    print("Average score:",round(computer_science[0]))
    print("best score:",computer_science[1])

    print("best score's stuednt id:",computer_science[2])

    print("number of stuudents eho passed:",computer_science[3])
    
    print()

    print("mathematical_anlysis1:")

    print("Average score:",round(mathematical_anlysis1[0]))
    print("best score:",mathematical_anlysis1[1])

    print("best score's stuednt id:",mathematical_anlysis1[2])

    print("number of stuudents eho passed:",mathematical_anlysis1[3])

    print()
    
    print("geometry:")

    print("Average score:",round(geometry[0]))
    print("best score:",geometry[1])

    print("best score's stuednt id:",geometry[2])

    print("number of stuudents eho passed:",geometry[3])
        

def main():

    students = read_students_file("students.txt")
    computer_science = process_computer_science(students)
    mathematical_anlysis1 = process_mathematical_anlysis1(students)
    geometry = process_geometry(students)
    print_results(computer_science,mathematical_anlysis1,geometry)
    
    

if __name__ == "__main__":
    main()