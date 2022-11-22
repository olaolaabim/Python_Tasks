#1 Writ a function which generates a six digit/character random_user_id.
from random import random, randint
import string
def random_user_id():
    letters =string.ascii_letters
    numbers= string.digits
    let_nums = letters + numbers
    let_nums_list = []
    for i in let_nums:
        let_nums_list.append(i)
    user_id = ''
    for i in range(6):
        index = randint(1, 61)
        user_id += (let_nums_list[index])
    return((user_id))
print(random_user_id())
#2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    no_of_ids = int(input("Enter the number of ids: "))
    no_of_character = int(input("Enter the number of characters"))
    for i in range(no_of_ids):
        letters = string.ascii_letters
        numbers = string.digits
        let_nums = letters + numbers
        let_nums_list = []
        for i in let_nums:
            let_nums_list.append(i)
        user_id = ''
        for i in range(no_of_character):
            index = randint(1, 61)
            user_id += (let_nums_list[index])
        print(user_id)

#print(user_id_gen_by_user())
#3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    color = []
    count = 0
    while count < 3:
        rang_col = randint(0, 256)
        color.append(rang_col)
        count += 1
    color = tuple(color)
    color = "rgb" + str(color)
    print(color)

#print(rgb_color_gen())

#Exercise level 2
#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(color_nums):
    letter = 'ABCDEF'
    numbers= string.digits
    alph = numbers + letter
    color_list = []
    for i in range(color_nums):
        color = '#'
        for j in range(6):
            hex_no = randint(0, 15)
            [color+alph[hex_no]]
        color_list.append(color)
    return (color_list)
list_of_hexa_colors(3)
#3 Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(rgb, num):
    tot_color = []
    for i in range(num):
        color = []
        count = 0
        while count < 3:
            rang_col = randint(0, 256)
            color.append(rang_col)
            count += 1
        color = tuple(color)
        color = rgb + str(color)
        tot_color.append(color)
    return tot_color
print(generate_colors('rgb',3))

def function_list(list_p):
    list_p = set(list_p)
    return list_p

print(function_list([1,2,54,56,8,67,7]))

