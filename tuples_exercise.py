#Exercise level 1
#1 Create an empty tuple
empty_tuple = ()
empty_tuple1 = tuple()
#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('farouk', 'khalid')
sisters =('teju', 'tinu', 'teni')
#3 Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
#4 How many siblings do you have?
siblings_len = len(siblings)
print(siblings_len)
#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('lanre')
siblings.append('nike')
family_members = tuple(siblings)
print(siblings)

#Exercises: Level 2
#1 Unpack siblings and parents from family_members
family_members = list(family_members)
siblings = family_members[0:5]
parents = family_members[5:7]
print(tuple(siblings),tuple(parents))

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('milk','beef','beacon','pork')
print('/'.join(fruits))
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp_list = list(food_stuff_tp)
print(food_stuff_tp_list)
#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
len_food = len(food_stuff_tp_list)
print(len_food)
print(food_stuff_tp_list[7])
#5 Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp_list[0:3])
print(food_stuff_tp_list[10:13])
#6 Delete the food_staff_tp tuple completely
del food_stuff_tp_list
#7 Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' is nordic_countries)
print('iceland' in nordic_countries)