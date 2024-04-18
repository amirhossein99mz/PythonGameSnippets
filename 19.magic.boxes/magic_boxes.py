def read_action(filename):
    try:
        actions = []
        with open(filename) as file:
            f = file.read().split("\n")
        for line in f:
            line = line.split()
            actions.append(line[-1])
        
        return actions
    
    except OSError as err:
        print(err)

def process(actions):
    
    
    box1 = []
    box2 = []
    magic_boxes = []

    for i in range(len(actions)):
       
        if len(box1) == 0:
            box1.append(actions[0])
        
        elif len(box1)!= 0 and  i % 2 == 0 and actions[i] == box1[0]:
            box1.append(actions[i])
        
        #elif len(box1) == 2:


       
        elif i == 1:
            box2.append(actions[i])
        elif i != 1 and i % 2 != 0 and actions[i] == box2[0]:
            box2.append(actions[i])
        
        else:
            if i == len(actions)-1:
                print(f"Generates no errors, as the box with the first BANANA is emptied and can later store a {actions[i]}")
      
    


        
    
    

    
       




def main():

    actions =  read_action("actions-simple.txt")
    process(actions)


if __name__ == "__main__":
    main()