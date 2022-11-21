#Exercise 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1 Find the length of the set it_companies
# sets
len_it_companies = len(it_companies)
print(len_it_companies)
#2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['info tech', 'instagram', 'enhanceIT'])
print(it_companies)
#4 Remove one of the companies from the set it_companies
it_companies.remove('instagram')#raises an error if the item does not exist
print(it_companies)
#5 What is the difference between remove and discard
it_companies.discard('enhance IT')#dos not raise an error

#Exercises Level 2
#1 Join A and B
C = A.union(B)
print(C)
#2 Find A intersection B
D = A.intersection(B)
print(D)
#3 Is A subset of B
print(A.issubset(B))
#4 Are A and B disjoint sets
print(A.isdisjoint(B))
#5 Join A with B and B with A
#(A.update(B))
#(B.union(A))
print(A)
print(B)
#6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#7 Delete the sets completely
del A
#Exercise Level 3
#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = set(age)
print(ages)
print(len(age) > len(ages))
#2 Explain the difference between the following data types: string, list, tuple and set
#String: are used for alphabets
#List: are immutable container for any kind of datatype
#Tuple: are mutable container for any kind of datatype
#set are containner for unique elements.

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
word = 'I am a teacher and I love to inspire and teach people.'
split_word=word.split(' ')
split_word = set(split_word)
len_split_word = len(split_word)
print(len_split_word)