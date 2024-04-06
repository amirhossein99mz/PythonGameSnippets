def read_morse_file(file_name):
    
    try:
        morse = {}
        morse2 = {}
        with open(file_name) as file:
            for line in file:
                id,code = line.strip().split()
                morse[id] = code
                morse2[code] = id
        
        return morse,morse2
    
    except OSError as err:
        print(err)

def read_command_file(file_name):
    
    try:
        with open(file_name) as file:
            f = file.read().split("\n")
        commands = []
        for line in f:
            line = line.split()
            commands.append(line)
        
        return commands
    
    except FileNotFoundError as err:
        print(err)

def encode(commands,morse):
    
    for i in range(len(commands)):
        for j in range(len(commands[i])):
            if commands[i][j] == "e":
                file_name = commands[i][j+1]
    
    try:
        encode = []
        with open(file_name) as file:
            f = file.read().split("\n")
        for line in f:
            for el in line:
                if el == " " or el == "!":
                    continue
                else:
                    encode.append(el.upper())
        
        encode2 = []
        for el in encode:
            if el in morse:
                encode2.append(morse[el])
        
        return encode2
        
    except ValueError as err:
        print(err)


def decode(commands,morse2):
    
    for i in range(len(commands)):
        for j in range(len(commands[i])):
            if commands[i][j] == "d":
                file_name = commands[i][j+1]
    
    try:
        decode = []
        with open(file_name) as file:
            f = file.read().split("\n")
        
        for line in f:
            line = line.split()
            for el in line:
                    decode.append(el)
        
        
        deocde2 = []
        
        for el in decode:
            if el in morse2:
                deocde2.append(morse2[el])
        
        return deocde2

        
        
    except ValueError as err:
        print(err)


def print_outputs(encoded,decoded):
    
    print("Encoding file text.txt:")
    for el in encoded:
        print(el,end=" ")
    
    print()

    print("Decoding file encoded.txt:")
    for el in decoded:
        print(el,end="")


def main():
    
    morse,morse2 = read_morse_file("morse.txt")
    commands = read_command_file("commands.txt")
    encoded = encode(commands,morse)
    decoded = decode(commands,morse2)
    print_outputs(encoded,decoded)

if __name__ == "__main__":
    main()