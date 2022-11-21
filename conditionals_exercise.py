#Exercise 1
#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

age = int(input("Enter your age: "))
driving_age = 18
if age > driving_age:
    print("You are old enough to learn to drive.")
else:
    more_years = driving_age - age
    print("You need " + str(more_years) + " years to learn to drive.")

#2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
your_age = int(input("Enter your age: "))
my_age = 32
if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am older than you with 1 year")
    else:
        print("I am older than you with " + str(diff) + " years" )
elif my_age < your_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are older than me with 1 year")
    else:
        print("You are older than me with " + str(diff) + " years")
else:
    print("we are age mates")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(str(a) + " is greater than b " + str(b))
elif a < b:
    print(str(a) + " a is lesser than b " + str(b))
else:
    print(str(a) + " is equal to " + str(b))

#Exercise 2
#Write a code which gives grade to students according to theirs scores:
score = 589

if score >= 80 and score <= 100:
    print("A")
elif score >= 70 and score <= 79:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("D")
elif score >= 0 and score <= 49:
    print("F")
else:
    print("Not a valid number")

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
season = input("Enter your current season: ").lower()

if season == 'september' or season == 'october' or season == 'november':
    print('The season is Autumn')
elif season == 'december' or season == 'january' or season == 'february':
    print('The season is Winter')
elif season == 'march' or season == 'april' or season == 'may':
    print('The season is Spring')
elif season == 'june' or season == 'july' or season == 'august':
    print('The season is Summer')
else:
    print("Invalid season")

#3 The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
sample_fruit = 'banana'

if sample_fruit not in fruits:
    fruits.append(sample_fruit)
    print('The  list has been modified: ', fruits)
else:
    print("The " + sample_fruit + " fruit already exist")

#4 Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys():
    skills_list= person['skills']
    print(skills_list[2])
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person.keys():
    skills_list = person['skills']
    if 'Python' in skills_list:
        print("He has Python")
# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person.keys():
    skills_list = person['skills']
    if 'React' in skills_list and 'Javascript' in skills_list:
        print('He is a front end developer')
    elif  'Node' in skills_list and 'Python' in skills_list and 'MongoDB' in skills_list:
        print('He is a backend developer')
    elif 'React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
        print('He is a fullstack developer')
    else:
        print('unknown title')
# * If the person is married and if he lives in Finland, print the information in the following format:
if 'is_marred' in person.keys() and 'country' in person.keys():
    status = person['is_marred']
    country = person['country']
    if status == True and country == 'Finland':
        first_name = person['first_name']
        last_name = person['last_name']
        print(first_name + last_name + " lives in " + country +". He is married" )

