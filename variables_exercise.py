#------------------LEVEL 1------------------

#1 The current file
#2 Day 2:30 Days of Python programming
#3 Declare a first name variable and assign a value to it
first_name = 'Rilwan'
#4 Declare a last name variable and assign a value to it
last_name = 'Abimbola'
#5 Declare a full name variable and assign a value to it
full_name = 'Rilwan Abimbola'
#6 Declare a country variable and assign a value to it
country = 'Nigeria'
#7 Declare a city variable and assign a value to it
city= 'Lagos'
#8 Declare an age variable and assign a value to it
age = 32
#9 Declare a year variable and assign a value to it
year = 2020
#10 Declare a variable is_married and assign a value to it
is_married = True
#11 Declare a variable is_true and assign a value to it
is_true = False
#12 Declare a variable is_light_on and assign a value to it
is_light_on = True
#12 Declare multiple variable on one line
a, b, c = 4, "james", True

#----------------------LEVEL 2----------------------------

#1 Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print((type(is_true)))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))
#2 Using the len() built-in function, find the length of your first name
print(len(first_name))
#3 Compare the length of your first name and your last name
print(max(len(first_name), len(last_name)))
print(min(len(first_name), len(last_name)))
#4 Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
    #4i Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
    #4ii Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
    #4iii Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
    #4iv Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
    #4v Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
    #4vi Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
    #4vii Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
#5 The radius of a circle is 30 meters.
rad = 30
    #5i Calculate the area of a circle and assign the value to a variable name of area_of_circle
pi = 3.142
area_of_circle = pi * rad * rad #pi * (rad**2)
    #5ii Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * rad
    #5iiiTake radius as user input and calculate the area.
rad = int(input("Enter the radius of the circle"))
area_of_circle = pi * rad * rad
#6 Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
country = input("Enter your country:")
age = int(input("Enter your age:"))
#7 Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')