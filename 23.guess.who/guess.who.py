def read_characters(filename):
      try:
            char = {}
            with open(filename) as file:
                  for line in file:
                        line = line.strip().split(";")
                        if line[0] == "Name":
                            pass
                        else:
                            char[line[0]] = {"Gender":line[1],"Hair color":line[2],"Hair length":line[3],"Glasses":line[4],"Hat":line[5],"Mustache":line[6],"Beard":line[7],"Bald":line[8]}
            return char
    
      except OSError as err:
            print(err)


def read_question1(filename):
      try:
            question1 = []
            with open(filename) as file:
               f = file.read().split("\n")
            for line in f:
                  line = line.split("=")
                  line = [i.strip() for i in line]
                  question1.append(line)
                 
            return question1
      
      except OSError as err:
           print(err)


def compare(characters,question1):
     
      q1 = question1[0]
      q2 = question1[1]
      q3 = question1[2]
     
     
      char2 = {}

      for key,value in characters.items():
            if value[q1[0]] == q1[1]:
               char2[key] = value
      

      
      char3 = {}

      for key,value in char2.items():
            if value[q2[0]] == q2[1]:
                 char3[key] = value

      
      char4 = {}

      for key,value in char3.items():
            if value[q3[0]] == q3[1]:
                 char4[key] = value
      
      
      #print result:

      print("Game characters:")


      for key,value in characters.items():
            print(f"{key} - Gender : {value['Gender']} - Hair color : {value[ 'Hair color']} - Hair length : {value[ 'Hair length']}",end =" ")
            
            if value[ 'Glasses'] == 'YES':
               print(", Glasses",end=" ")
                 
            if value[ 'Hat'] == 'YES':
                print(", Hat",end=" ")
            
            if value[ 'Mustache'] == 'YES':
               print(", Mustache",end=" ")
            
            if value[ 'Beard'] == 'YES':
                print(", Beard",end=" ")

            if value[ 'Bald'] == 'YES':
               print(", Bald",end=" ")
      
            print()
      
      print()

      print("step1 - question: Hair color = Blond")
      print("Selected characters:")

      for key,value in char2.items():
            print(f"{key} - Gender : {value['Gender']} - Hair color : {value[ 'Hair color']} - Hair length : {value[ 'Hair length']}",end =" ")
            
            if value[ 'Glasses'] == 'YES':
               print(", Glasses",end=" ")
                 
            if value[ 'Hat'] == 'YES':
                print(", Hat",end=" ")
            
            if value[ 'Mustache'] == 'YES':
               print(", Mustache",end=" ")
            
            if value[ 'Beard'] == 'YES':
                print(", Beard",end=" ")

            if value[ 'Bald'] == 'YES':
               print(", Bald",end=" ")
      
            print()
      print()

      

      print("Step 2 - question: Hair length = Short")
      print("Selected characters:")

      for key,value in char3.items():
            print(f"{key} - Gender : {value['Gender']} - Hair color : {value[ 'Hair color']} - Hair length : {value[ 'Hair length']}",end =" ")
            
            if value[ 'Glasses'] == 'YES':
               print(", Glasses",end=" ")
                 
            if value[ 'Hat'] == 'YES':
                print(", Hat",end=" ")
            
            if value[ 'Mustache'] == 'YES':
               print(", Mustache",end=" ")
            
            if value[ 'Beard'] == 'YES':
                print(", Beard",end=" ")

            if value[ 'Bald'] == 'YES':
               print(", Bald",end=" ")
      
            print()
      print()

      print("Step 3 - question: Glasses = YES")

      print("Selected characters:")

      for key,value in char4.items():
            print(f"{key} - Gender : {value['Gender']} - Hair color : {value[ 'Hair color']} - Hair length : {value[ 'Hair length']}",end =" ")
            
            if value[ 'Glasses'] == 'YES':
               print(", Glasses",end=" ")
                 
            if value[ 'Hat'] == 'YES':
                print(", Hat",end=" ")
            
            if value[ 'Mustache'] == 'YES':
               print(", Mustache",end=" ")
            
            if value[ 'Beard'] == 'YES':
                print(", Beard",end=" ")

            if value[ 'Bald'] == 'YES':
               print(", Bald",end=" ")
      
            print()
      print()
      

      if len(char4) == 1:
          print("Congratulations, you win! Character selected:")
      
      for key,value in char4.items():
            print(f"{key} - Gender : {value['Gender']} - Hair color : {value[ 'Hair color']} - Hair length : {value[ 'Hair length']}",end =" ")
            
            if value[ 'Glasses'] == 'YES':
               print(", Glasses",end=" ")
                 
            if value[ 'Hat'] == 'YES':
                print(", Hat",end=" ")
            
            if value[ 'Mustache'] == 'YES':
               print(", Mustache",end=" ")
            
            if value[ 'Beard'] == 'YES':
                print(", Beard",end=" ")

            if value[ 'Bald'] == 'YES':
               print(", Bald",end=" ")
      
            print()
      print()



def main():
    
    chararcters = read_characters("characters.txt")
    
    question1 = read_question1("question1.txt")

    compare(chararcters,question1)


if __name__ == "__main__":
    main()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
  