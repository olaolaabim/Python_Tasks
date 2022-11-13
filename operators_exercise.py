#Day 3
import math

#1 Declare your age as integer variable
age = 7
#2 Declare your height as a float variable
height = 6.1
#3 Declare a variable that store a complex number
complex_no = 3+7j
#4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base:"))
height = int(input("Enter height:"))
area_triangle = 0.5 * base * height
print("The area of the triangle is: " + str(area_triangle))
#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Enter side a:"))
side_b = int(input("Enter side b:"))
side_c = int(input("Enter side c:"))
perimeter_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is " + str(perimeter_triangle))
#6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter the length:"))
width = int(input("Enter width:"))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("The perimeter of the rectangle is " + str(perimeter_rectangle))
print("The area of the rectangle is " + str(area_rectangle))
#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter the radius of the circle:"))
pi = 3.142
area_circle = pi * radius * radius
print("The area of the circle is " + str(area_circle))
#8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
#m = (y2-y1)/(x2-x1)
# y = (-2,0)
# x = (1,0)
y2 = -2
y1 = 0
x2 = 1
x1 = 0
m1 = (y2-y1)/(x2-x1)
print(m1)
#9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
y2 = 2
y1 = 2
x2 = 6
x1 =10
m2 = (y2-y1)/(x2-x1)
d = math.sqrt(((x2-x1)**2)+((x2-x1)**2))
print("The slope os ", m2)
print("The euclidean distance is ", d)
#10 Compare the slopes in tasks 8 and 9.
print(m1>m2, m1<m2)
#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
x = int(input("Enter the value of x"))
y = (x**2) + (6*x) + 9
print("The value of y:", y)
# y is zero when x is -3

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = "python"
dragon = "dragon"
print(len(python) > len(dragon))
#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print ('on' in python and 'on' in dragon)
#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")
#15 There is no 'on' in both dragon and python
print ('on' not in python and 'on' not in dragon)
#16 Find the length of the text python and convert the value to float and convert it to string
(word_len) = len(python)
f_word_len = float(word_len)
s_word_len = str(f_word_len)
#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
#using %
rem = 7%2
#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
f_div = 7//3
num = 2.7
print(int(num) is f_div)
#19 Check if type of '10' is equal to type of 10
print(type('10') is type(10))
#20 Check if int('9.8') is equal to 10
print(int(9.8) is 10)
#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hours: "))
print("Your weekly earning is: ", (hours*rate))
#22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
print("You have : ", (years*365*24*60*60))
#23 Write a Python script that displays the following table
print (1,1,1,1,1)
print(2,1,2,4,8)
print(3,1,3,9,27)
print(4,1,4,16,64)
print(5,1,5,25,125)
