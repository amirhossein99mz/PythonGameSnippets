print("wlecome to mutiple program, Let's go ")

#armstrong
print("armstrong")
def isArmstrong(number):
    return number == sum(int(i)**len(str(number)) for i in str(number))

def isvalid():
    lst = []
    
    while True:
        num = int(input("Enter a num:"))
        if num == -1:
            break
        if isArmstrong(num):
            lst.append(num)
    return lst
print(isvalid())





#delete prime number
print("delete prime number")
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def isvalid():
    
    num = int(input("a number:"))
    if is_prime(num):
        print(num)
   
isvalid() 





#christamss tree
print("christmas tree")
def christmass_tree(height):
    
    for i in range(height+1):
        space = " "*(height-i)
        star = "*"*((2*i)-1)
        print(space+star)

christmass_tree(int(input("a number:")))
    




#fib sequence
print("fibonachi_sequence")
def fib_sequence():
    fib = [0,1]
    num = int(input("enter a number:"))
    for i in range(num):
        fib.append(fib[-1]+fib[-2])
    print(fib)
fib_sequence()




#pascal triangle
print("pascal triangle")
def pascalTriangle(n):
    matrix = [[1]]
    
    for i in range(n):
        new = [1]
        
        for j in range(len(matrix[-1])-1):
            new.append(matrix[-1][j]+matrix[-1][j+1])
        new.append(1)
        matrix.append(new)
    
    for i in range(len(matrix)):
        print(" ".join(str(x) for x in matrix[i]))

pascalTriangle(int(input(("Enter a num:"))))




#sort method
print("sort method")
def sort_method():
    
    list1 = [2,54,12,87,98,23]
    list2 = []

    for i in range(len(list1)):
        s = None
        for j in list1:
            if s == None:
                s = j
            else:
                if j < s:
                    s = j
        list2.append(s)
        list1.remove(s)
                
    return list2
print(sort_method())

#matrix
import random as r

def cearteMatrix():
    row = int(input("Enter a number as row:"))
    col = int(input("Enter a number as col:"))

    matrix = []

    for i in range(row):
        new = []
        for j in range(col):
            z = r.randint(1,9)
            new.append(z)
        matrix.append(new)
    
    for i in range(len(matrix)):
        print(" ".join(str(x)) for x in matrix[i])
    
    main_diag = [matrix[i][i] for i in range(min(row,col))]

    sub_diag = [matrix[i][-1-i] for i in range(min(row,col))]

    first_col = [row[0] for row in matrix]

    last_col = [row[-1] for row in matrix]

    print(main_diag)
    print()
    print(sub_diag)
    print()
    print(first_col)
    print()
    print(last_col)

cearteMatrix()