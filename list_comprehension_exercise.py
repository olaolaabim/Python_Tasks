#1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filt_nums = [i for i in numbers if i <= 0]
print(filt_nums)
#2 Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = [number for row in list_of_lists for i in row for number in i]
print(output)
#3 Using list comprehension create the following list of tuples:
rand_list = [(i, 1, i, (i*i),(i**3),(i**4),(i**5) )for i in range(11)]
print(rand_list)
#4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [list(country) for item in countries for country in item ]
[item.insert(1,(flat_countries[0][0][0:3])) for item in flat_countries ]
print(flat_countries)
#5 Change the following list to a list of dictionaries:
key_list = ["country", "city"]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{key_list[0]: country[0],key_list[1]: country[1]} for row in countries for country in row ]
print(dict_countries)
#6 Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_list = [name[0] + " " + name[1] for item in names for name in item]
print(names_list)
#7 Write a lambda function which can solve a slope or y-intercept of linear functions.
x=0
y = lambda m, b: (m*x) + b
print(y(2,4))