x = {} # empty dictionary

student = {
    'name' : 'farhan',
    'course' : 'BCA',
    'aeg' : 200,
    'isAdult' : True,
    'subjects' : ['c', 'python' , 'javascript', 'machine learning'],
    'certificates' : {
        '2021': 'apna college',
        '2022': 'google cloud',
        '2026': 'claude architect'
    } 
}

# print(x)
# print(type(x))
# print(student)
# print(student['name'])
# print(student['subjects'])
# # print(student['city']) # keyError
# print(student['certificates']['2021'])

# print(student.get('name'))
# print(student.get('city'))
# print(student.get('city', 'not found'))


# print(student.keys())
# print(list(student.keys()))
# print(student.values())
# print(list(student.values()))
# print(student.items())
# print(student.update('age':21))
# print(student.pop('courses'))
# print(student.clear())


# student['city'] = 'agra'
 
# for key , values in student.items():
#     print(key, values)

# for key in student:
#     print(key)

# for values in student:
#     print(values)


# comprehensions (work for both list and dictionaries)

x = [x for x in range(10)]
print(x)
y = [0 for y in range(10)]
print(y)
z = [z + 5 for z in range(10)]
print(z)
w = [[0 for w in range(5)] for w in range(5)]
print(w)
u = [i for i in range(100) if i % 5 == 0]
print(u)