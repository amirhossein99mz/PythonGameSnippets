def read_events(filename):
    try:
        events = []
        with open(filename) as file:
            for line in file:
                day,hour,event = line.strip().split(";")
                events.append([int(day),hour,event])
        
        return events
        
    except OSError as err:
        print(err)


def read_commands(filename):
    try:
        commands = []
        with open(filename) as file:
            f = file.read().split("\n")
        
        for line in f:
            line  = line.split()
            line[1] = int(line[1])
            if len(line) == 2:
                i = len(line)
                while i < 5:
                    line.append(0)
                    i += 1
                    if i == 5:
                        break
            commands.append(line)

        return commands   
        
    except OSError as err:
        print(err)


def process(events,commands):

   
    
    proccessed = []
    list1 = []

    for i in range(len(commands)):
        for j in range(len(events)):
            if commands[i][0] == 'v':
                list1.append(commands[i][1])
                if commands[i][1] == events[j][0]:
                    list1.append("Events of day")
                    list1.append(events[j][1])
                    list1.append(":")
                    list1.append(events[j][2])
                    proccessed.append(list1)
                list1 = []
            
            else:
                if commands[i][1] == events[j][0]:
                    k = events[j][0]
                    proccessed.append(["Cannot insert event"])
                
                if commands[i][1] not in events[j]:
                    list1 = ["Event inserted"]
                    list1.append(commands[i][1])
                    list1.append(commands[i][2])
                    list1.append(commands[i][3]+" "+commands[i][4])

                    
                   
    proccessed.append(list1)   
   
    return proccessed          




def main():

    events = read_events("events.txt")
    
    commands = read_commands("commands.txt")
    
    result = process(events,commands)
    

    print("Events of day ",end=" ")
    print(result[1][0],end=" ")
    print(":")
    print(result[1][2],":",end=" ")
    print(result[1][-1])
    print(result[0][2],":",end=" ")
    print(result[0][-1])

    result.pop(0)
    result.pop(0)
    
    for el in result:
        if len(el) == 1:
            for i in el:
                print(i,end=" ")
            print()
        else:
            print(el[0])
            print("Events of day",el[1],":")
            print("    ",el[-2],el[-1])
    
    
    

if __name__ == "__main__":
    main()