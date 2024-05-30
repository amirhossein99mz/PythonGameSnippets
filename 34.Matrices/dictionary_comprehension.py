#dictionary comprehension in Python

#dictionary_2 = {key:(expression) for (key,value) in dictionary.items()}
#dictionary_2 = {key:(expression) for (key,value) in dictionary.items() if ..... else .....}
#dictionary_2 = {key:(..... if .... else ....) for (key,value) in dictionary.items()}


#Ex1)

#d1 = {"Torino":{"temp":18,"rain":4},"Milano":{"temp":13,"rain":8}}
#d2 = {key:round(value["rain"]*2) for (key,value) in d1.items() if value["temp"]==18}
#d3 = {key:("warm" if value["temp"] > 40 else "cold") for key,value in d1.items()}




students = {"ali":{"height":190,"wei":90},"hasan":{"height":187,"wei":80},"amir":{"height":195,"wei":100}}

print({key:("Tall" if value["height"]>= 190 else "short") for (key,value) in students.items()})
print()
a = {key:("fat" ) for (key,value) in students.items() if (value["wei"] > 10) }

print(a)
