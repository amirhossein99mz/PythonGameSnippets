num = int(input("Enter a number: "))

for i in range(num-1):
    print('*' * num)
print()

print("christamss tree:")
print()

for i in range(num):

    print(" "*(num-i)+"*"*((2*i)+1))

for i in range(num,0,-1):
    print(" "*(num-i)+"*"*((2*i)+1))
# how to print christmas tree in puython