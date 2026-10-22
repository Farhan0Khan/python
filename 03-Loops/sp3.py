students = [
    {"name":"Harry","house":"Gryffindoor","patronus":"Stag"},
    {"name":"Hermoinee","house":"Gryffindoor","patronus":"Otter"},
    {"name":"Ron","house":"Gryffindoor","patronus":"Jack"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]

for i,student in enumerate(students):
    print(i,student["name"], student["house"] , end="\n" , sep=" | ")