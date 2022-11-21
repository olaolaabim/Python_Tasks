#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty " + "Days " + "Of " + "Pyhon")
#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding " + "for " + "all")
#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = 'coding for all'
#4 Print the variable company using print().
print(company)
#5 Print the length of the company string using len() method and print().
print(len(company))
#6 Change all the characters to uppercase letters using upper() method.
company.upper()
#7 Change all the characters to lowercase letters using lower() method.
company.lower()
#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company.capitalize()
company.title()
(company.swapcase())
#9 Cut(slice) out the first word of Coding For All string.
print(company[slice(7,15)])
#10 Check if Coding For All string contains a word Coding using the method index, find or other methods
word = 'laugh'
string = 'This is laughing laugh'.split(" ")
index = string.index(word)
print(index)
#11 Replace the word coding in the string 'Coding For All' to Python.
string1 = 'coding for all'
print(string1.replace('coding', 'python'))
#12 Change Python for Everyone to Python for All using the replace method or other methods.
every = 'python for everyone'
print(every.replace('everyone', 'all'))
#13 Split the string 'Coding For All' using space as the separator (split()) .
string1.split(" ")
#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
corp = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
corp.split(',')
#15 What is the character at index 0 in the string Coding For All.
print(string1[0])
#16 What is the last index of the string Coding For All.
s= len(string1)-1
print(string1[s])
#17 What character is at index 10 in "Coding For All" string.
print(string1[10])
#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
# get all words
acronym = "Python For Everyone"
lst = acronym.split()
output = ""
# iterate over words
for word in lst:
    # get first letter of each word
    output += word[0]
# uppercase oupt
output = output.upper()
print(output)
#19 Create an acronym or an abbreviation for the name 'Coding For All'.
# add first letter
acronym1 = 'Coding For All'
output1 = acronym1[0]
# iterate over string
for i in range(1, len(acronym1)):
    if acronym1[i - 1] == ' ':
        # add letter next to space
        output1 += acronym1[i]
# uppercase oupt
output1 = output1.upper()
print(output1)
#20 Use index to determine the position of the first occurrence of C in Coding For All.
string2 = 'Coding For All'
print(string2.find('C'))
#21 Use index to determine the position of the first occurrence of F in Coding For All.
print(string2.find('F'))
#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
string3 = 'Coding For All People'
print(string3.rfind('l'))
#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
sentence_split = sentence.split()
print(sentence_split.index('because'))
#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', ''))
#28 Does ''Coding For All' start with a substring Coding?
string = 'Coding For All'
print(string.startswith('Coding'))
#29 Does 'Coding For All' end with a substring coding?
print(string.endswith('coding'))
#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
print(string.strip(' '))
#31 Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(lib_list))
#33 Use the new line escape sequence to separate the following sentences
print('I am enjoying this challenge.\nI just wonder what is next.')
#34 Use a tab escape sequence to write the following lines.
print('Name\t Age\t Country\t City')
print('Asabenech\t 250\t Finland\t Helsinki')
#35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
pri = "The area of a circle with radius " + str(radius) + " is " + str(area) + "meters square."
print(pri)
#36 Make the following using string formatting methods:
print (
'8 + 6 = 14 \n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')