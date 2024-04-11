def readStudentsFile(filename):
    try:
        f = open(filename)
    except OSError as e:
        print(f"The error is {e}")
    

    file = f.read().split("\n")
    
    f.close()
    
    matrice = []

    for line in file:
        line = line.split()
        matrice.append(line)

    return matrice

def process(students):
    lessons = students[0]
    students.pop(0)
    

    result = {}

    for line in students:
        result[line[0]] = {lessons[0]:line[1],lessons[1]:line[2],lessons[2]:line[3]}
    
    for key,value in result.items():
        
        if value['computerScience'] == '30L':
            value['computerScience'] = 33
        else:
            value['computerScience'] = int(value['computerScience'])


        if value['MathematicalAnlysis1'] == '30L':
            value['MathematicalAnlysis1'] = 33
        else:
            value['MathematicalAnlysis1'] = int(value['MathematicalAnlysis1'])

        
        if value['Geometry'] == '30L':
            value['Geometry'] = 33
        else:
            value['Geometry'] = int(value['Geometry'])
    
    
    
    resultn = {}
    
    for el in lessons:

        resultn[el]={'numberOfPassed':0,'sum':0,'best_grade':0,'student_best_grade':None}
            
    
    print()
    print()
    print()
    
    max_grade = 0
    best_person = None

    for key,value in result.items():
        for keyn,valuen in resultn.items():
            if value[keyn] >= 18:
                valuen['numberOfPassed'] += 1
            valuen['sum'] += value[keyn]
    
           
    max_com = 0
    max_com_name = None

    max_math = 0
    max_math_name = None

    max_geo = 0
    max_geo_name = None

    

    for key,value in result.items():


        if value['computerScience'] > max_com:
            max_com =  value['computerScience'] 
            max_com_name = key

    
    
        if value['MathematicalAnlysis1'] > max_math:
            max_math =  value['MathematicalAnlysis1'] 
            max_math_name = key


    
        if value['Geometry'] > max_geo:
            max_geo =  value['Geometry'] 
            max_geo_name = key

    resultn['computerScience']['best_grade'] = max_com
    resultn['computerScience']['student_best_grade'] = max_com_name


    
    resultn['MathematicalAnlysis1']['best_grade'] = max_math
    resultn['MathematicalAnlysis1']['student_best_grade'] = max_math_name

    resultn['Geometry']['best_grade'] = max_geo
    resultn['Geometry']['student_best_grade'] = max_geo_name

   
    for key,value in resultn.items():
        print()
        print(f"{key} :")
        print(f"number of students who passed the exam: {value['numberOfPassed']}")
        print(f"sum of scores : {value['sum']}")
        print(f"student {value['student_best_grade']} got best score {value['best_grade']}")
    
            

    


def main():
    students = readStudentsFile('students.txt')
    process(students)


if __name__ == "__main__":
    main()