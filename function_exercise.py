#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_a, num_b):
    return (num_a + num_b)
print(add_two_numbers(2,3))

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(rad):
    area = 3.142 * rad * rad
    return area
print(area_of_circle(4))
#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(x, *y):
    sum_nums = x
    for i in y:   
        if type(i) == type(5):
            sum_nums += i       
        else:
            error ="Enter an integer in the list of number"
            return error
     
    return(sum_nums)
print(add_all_nums(1,2,3,4,5))

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def cel_to_fah(cel):
    fah = (cel * (9/5) + 32)
    return fah
print(cel_to_fah(34))

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(season):
    if season == 'september' or season == 'october' or season =='november':
        return('The season is Autumn')
    elif season == 'december' or season == 'january' or season == 'february':
        return('The season is Winter')
    elif season == 'march' or season == 'april' or season == 'may':
        return('The season is Spring')
    elif season == 'june' or season == 'july' or season == 'august':
        return('The season is Summer')
    else:
        return("enter a valid month")
print(check_season('september'))
#6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(m,x,b):
    y = (m*x) + b 
    return y
import math
#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quad(a,b,c):
    x1 = abs(b*b) - (4*a*c)
    x1 = (math.sqrt(x1))
    x1 = -b + x1
    x1 = x1/(2*a)
    
    x2 = (b*b) - (4*a*c)
    x2 = math.sqrt(x2)
    x2 = -b - x2
    x2 = x2/(2*a)
    #x1 = (-b + math.sqrt((b*b) - (4*a*c)))/(2*a)
    #x2 = (-b - math.sqrt((b*b) - (4*a*c)))/(2*a)    
    return ("the squares are either " + x1 + "or" + x2 )


#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(d):
    for i in d:
        print(i)
    return i
h = [1,3,2,3,'the']
print(print_list(h))

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reverse_arr = []
    len_arr = len(arr)
    count = 0
    while count < len_arr:
        print(arr[len_arr-1])
        reverse_arr.append(arr[len_arr-1])
        len_arr -= 1
    return reverse_arr
    
print(reverse_list([12,26,33,45,51]))

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(c_list):
    cap_list= []
    for i in c_list:
        cap_list.append(i.upper())
    return cap_list
print(capitalize_list_items(['ali','simi', 'agon']))

#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(e_list, item):
    e_list.append(item)
    return e_list
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))

#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item( e_list, item):
    e_list.remove(item)
    return e_list
print(remove_item(numbers, 9))

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers (num_1):
    sum_nums = 0
    for i in range(0,num_1+1):
        sum_nums += i
    return sum_nums
print(sum_of_numbers(100))

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds (odd_num):
    sum_odds = 0
    for i in range(1,odd_num,2):
        sum_odds += i
    return sum_odds
print(sum_of_odds(5))

#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even (even_num):
    sum_evens = 0
    for i in range(0,even_num+1,2):
        sum_evens += i
    return sum_evens
print(sum_of_even(5))

#Exercise level 2
#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(pos_int):
    odd_list = []
    even_list = []
    for i in range(0, pos_int+1):
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
        len_odd = len(odd_list)
        len_even = len(even_list)
    return len_odd, len_even#("The number of odds are" +len_odd+ ".\nThe number of evens are " + len_even )
print(evens_and_odds(100))

#1 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(whole_num):
    fact = 1
    for i in range(1,whole_num+1):
        fact *= i
    return fact
print(factorial(5))
#2 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(par):
    if par == '' or par ==[] or par == () or par == {}:
        x = 'empty para'
    return x
x = []
print(is_empty(x))

#3 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def mean_calc(a_list):
    sum_a_list = 0
    len_a_list = len(a_list)
    for i in a_list:
        sum_a_list += i
    avg_a_list = sum_a_list/len_a_list
    return avg_a_list
print(mean_calc([1,2,3,4,5]))

#def mode_calc(a_list):

#1 Write a function called is_prime, which checks if a number is prime.
def is_prime(num_2):
    if num_2 % 2 != 0 and num_2 % 3 != 0 :
        return 'his is a prime number'
    else:
        return 'not prime'
print(is_prime(6))

#2 Write a functions which checks if all items are unique in the list.
def check_item(b_list):
    set_b_list = set(b_list)
    if len(b_list) == len(set_b_list):
        return "unique list"
    else:
        return "not a unique list"
print(check_item([1,1,2,2,2,1]))

#3 Write a function which checks if all the items of the list are of the same data type.
def check_type(c_list):
    d_type = []
    for i in c_list:
        d_type.append(type(i))
        #d_type.append(i)
    d_type = set(d_type)
    if len(d_type) == 1:
        return "they contain similar type"
    else:
        return "They do not contain similar type"

print(check_type([1,1,2,23,3,32,2]))