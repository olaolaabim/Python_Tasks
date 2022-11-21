#Exercise
#1 Create an empty dictionary called dog
dog = {}
print(dog)
#2 Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Olalekan', 'color': 'red', 'breed':'bulldog', 'legs': 'four', 'age': 32}
print(dog)
#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'Ola', 'last_name': 'Abimbola', 'gender':'male', 'age': 34, 'marital_status': 'Married', 'skills': ['Html', 'Sql', 'java'], 'country':'Nigeria', 'city':'Ibadan', 'address': '12 fatai abimbola close, ishasi rd'}
print(student)
#4 Get the length of the student dictionary
print(len(student))
#5 Get the value of skills and check the data type, it should be a list
x = student['skills']
print(type(x))
#6 Modify the skills values by adding one or two skills
student['skills'].append('python')
student['skills'].append('Scala')
print(student['skills'])
#7 Get the dictionary keys as a list
y = student.keys()
print(y)
#8 Get the dictionary values as a list
z = student.values()
print(z)
#9 Change the dictionary to a list of tuples using items() method
stud_tuple= student.items()
print(tuple(stud_tuple))
#10 Delete one of the items in the dictionary
student.pop('first_name')
print(student)
student.popitem()
print(student)
#11 Delete one of the dictionaries
del student