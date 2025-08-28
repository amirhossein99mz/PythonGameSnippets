def is_armstrong_number(number):
    number = str(number)

    count = 0

    for i in range(len(number)):
        count += (int(number[i])**len(number))

    if int(count) == int(number):
        return True
    else:
        return False

def is_prime(number):

    number = int(number)

    if number < 2:
        return False

    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def main():

    lst = []
    while True:
        num = int(input("Enter a number or -1 to stop:"))
        if num == -1:
            break
        lst.append(num)

    max = 0

    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    
    print(max)
    if  is_armstrong_number(max):
        print("The number is armstrong")
    else:
        print("The number is NOT armstrong")
    
    if is_prime(max):
        print("The number is prime")
    
    else:
        print("The number is NOT prime")

main()