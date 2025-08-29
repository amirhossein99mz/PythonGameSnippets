def readEventsFile(EventsFile):
    
    try:
        
        f = open(EventsFile)
    
    except OSError as e:

        print(f"The error is {e}")
    
    file = f.read().split("\n")
    
    events = []

    for line in file:

        line = line.split(";")

        line[0:1] = [int(i) for i in line[0:1]]

        events.append(line)
    
   
    
    return(events)
    

def readCommandsFile(commandsFile):
    
    try:
        
        f = open(commandsFile)
    
    except OSError as e:

        print(f"The error is {e}")
    
    file = f.read().split("\n")

    commands = []

    for line in file:
        line = line.split()
        
        if line[-1] != 'conference':
            line[1] = int(line[1])
            line.append(0)
            line.append("NoPressConference")
        
        else:

            line[1:3] = [int(i) for i in line[1:3]]
            line[-2] += line[-1]
            line.pop(-1)
        
        commands.append(line)

    return(commands)


def ProcessCalendar(events,commands):

    #events:
    #day : line[0]
    #hour : line[1]
    #descrption : line[2]

    a = events[1]
    events[1] = events[2]
    events[2] = a 

    for line in commands:

        if line[0] == 'v':
            
            print(f"Events of day {line[1]} :")
            
            for el in (events):
                
                if line[1] == el[0]:

                    print(f"   {el[1]} : {el[2]}")

        
        elif line[0] == 'i':

            for el in (events):

                if line[1] == el[0] :

                    print("cannot insert the event")
                
                else:

                    a = "event inserted"
                    b = f"Events of day {line[1]}:"
                    c = f"   {line[-2]}: {line[-1]}"
  
    print(a)
    print(b)
    print(c)
                


                
    



def main():


    events = readEventsFile("C:/Users/javan/OneDrive/Desktop/program/12.Done/events.txt")

    commands = readCommandsFile("C:/Users/javan/OneDrive/Desktop/program/12.Done/commands.txt")
    
    ProcessCalendar(events,commands)
    
    

if __name__ == "__main__":
    main()