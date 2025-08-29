def read_plotter(filename):
    try:
        matrix = []
        with open(filename) as file:
            f = file.read().split("\n")
        
        for line in f:
            line = line.split()
            if len(line) == 3:
                line.append(0)
            for i in range(len(line)):
                if i == 0:
                    continue
                else:
                    line[i] = int(line[i])
            matrix.append(line)
        
        for i in range(len(matrix)):
            matrix[i].append(0)
        
        return matrix
            
    except OSError as err:
        print(err)
    


def main():
    plotter = read_plotter("plotter.txt")

    for i in range(len(plotter)):
        if plotter[i][0] == 'P':
            plotter[i] = ['...|.']
        elif plotter[i][0] == 'H':
            if plotter[i][2] == 3:
                plotter[i] = ['..*|.']
            elif plotter[i][2] == 1:
                plotter[i] = ['.--+.']
        else:
            plotter[i] = [".*-+."]
        
    for line in plotter:
        for el  in line:
            print(el,end=" ")
        print()


if __name__ == "__main__":
    main()