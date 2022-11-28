countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Explain the difference between map, filter, and reduce.
#Map is used to operate on an iterable i.e. return the value of a function operation on a list while
#filter is used to check if the condition of a function is true while reduce an reduces an iterable based on the operation of a function.

#4 Use for loop to print each country in the countries list.
for i in countries:
    print(i)
#5 Use for to print each name in the names list.
for i in names:
    print(i)
#6 Use for to print each number in the numbers list.
for i in names:
    print(i)

#Exercise level 2
#1 Use map to create a new list by changing each country to uppercase in the countries list
upper_countries = map(lambda i: i.upper(), countries)
print(list(upper_countries))
#2 Use map to create a new list by changing each number to its square in the numbers list
sq_numbers = map(lambda i : i**2, numbers)
print(list(sq_numbers))
#3 Use map to change each name to uppercase in the names list
upper_names = map(lambda i: i.upper(), names)
print(list(upper_names))
#4 Use filter to filter out countries containing 'land'.
filt_countries = filter(lambda i:('land') in i ,countries)
print(list(filt_countries))
#5 Use filter to filter out countries having exactly six characters.
filt_countries = filter(lambda i:(len(i)==6), countries)
print(list(filt_countries))
#6 Use filter to filter out countries containing six letters and more in the country list.
filt_countries = filter(lambda i:(len(i)>=6), countries)
print(list(filt_countries))
#7 Use filter to filter out countries starting with an 'E'
filt_countries = filter(lambda i: i.startswith('E'), countries)
print(list(filt_countries))
#8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
chain_high = reduce(lambda x, y: x+y, filter(lambda i : i%2 ==0, map(lambda i : i ** 2, numbers)))
print((chain_high))
#9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
li = [2,2,3,4,'ghg','fgf']
get_strings_lists = filter(lambda x: type(x) == type('string'), li)
print(list(get_strings_lists))
#10 Use reduce to sum all the numbers in the numbers list.
sum_red = reduce(lambda x,y: x+y, numbers)
print(sum_red)
#11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
st = 'are north european countries'
concat_reduce =  reduce(lambda x, st: x + ', ' + st , countries)
print(concat_reduce)
#12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

#13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def dict_coun(country):
    key_list = country[0:3]
    return key_list
print(dict_coun('Denmark'))

#14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
#15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.