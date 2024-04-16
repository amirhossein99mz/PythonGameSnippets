def readPlotterFile(plotterFile):
    
    try:

        f = open(plotterFile)
    
    except OSError as e:
        
        print(f"The ERROR is {e}")
    
    file = f.read().split("\n")

    f.close()

    matrice = []

    for line in file:

        line = line.split()
        line[1:] = [int(i) for i in line[1:]]
        
        if len(line) == 3:

            line.append(0)

            line.append(0)
        
        elif len(line) == 4:

            line.append(0)

        matrice.append(line)
        
    return(matrice)


def process(plotter):

    for line in plotter:

        if line[0] == "V":

            if line[1] == 3 and line[-2] == 5:

                line[0] = "."
                line[1] = "*"
                line[2] = "-"
                line[3] = "+"
                line[4] = line[0]

        elif line[0] == "P":

            line[0:] = ['.','.','.','|','.']
        
        elif line[0] == "H":

            if line[2] == 3:
                #..*|.

                line[0:] = ['.','.','*','|','.']

            elif line[2] == 1:
                #.--+.

                line[0:] = ['.','-','-','+','.']
    
    for i in range(len(plotter)):

        print(" ".join(str(x) for x in plotter[i]))



def main():

    plotter = readPlotterFile("C:/Users/javan/OneDrive/Desktop/program/11.Done/plotter.txt")

    process(plotter)

main()