def read_events(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File does NOT exist.")
    events = []
    f =f.read().split('\n')
    for line in f:
        line = line.split(";")
        events.append(line)
    
    for line in events:
        line[0] = int(line[0])
        line[1] = int(line[1])
    return(events)


def read_command(filename1):
    try:
        f =open(filename1)
    except ValueError as e:
        print("cannot access file.")
    f = f.read().split("\n")
    commands = []
    for line in f:
        line = line.split()
        commands.append(line)
    print()
    commands[0].append(0)
    commands[0].append("Press_NO_conference")
    for i in range(len(commands)):
        commands[i].pop(0)
        commands[i][1] = int(commands[i][1])
        commands[i][0] = int(commands[i][0])
    commands[-1][-2] = commands[-1][-2] + commands[-1][-1]
    commands[-2][-2] = commands[-2][-2] + commands[-2][-1]
    commands[-1].pop(-1)
    commands[-2].pop(-1)
    return(commands)


def calendar(events,commands):
    
    lst = []
    for co in commands:
        for ev in events:
            if co[0] == ev[0] and co[-1] == 'Press_NO_conference':
                lst.append(ev[0])
                lst.append(ev[1])
                lst.append(ev[2])
            if co[0] == ev [0] and co[1] == ev[1] and co[2] != ev[2]:
                a = "cannot insert event." 
            elif co[0] != ev[0]:
                b = "event inserted"
                c = co[0]
                d = co[1]
                e = co[2]
             
    print(f"events of day {lst[0]}:")
    print(f"     {lst[4]}: {lst[5]}")
    print(f"     {lst[1]}: {lst[2]}")
    print(a)
    print(b)
    print(f"Events of day {c}:")
    print(f"    {d}: {e}")
def main():
    events = read_events("events.txt")
    commands = read_command('commands.txt')
    calendar(events,commands)
  

if __name__ == "__main__":
    main()
