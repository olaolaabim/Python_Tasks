#1 Declare an empty list
empty_list = []
empty_list = list()
#2 Declare a list with more than 5 items
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot', 'Spinach']
#3 Find the length of your list
print(len(vegetables))
#4 Get the first item, the middle item and the last item of the list
print(vegetables[0])
print(vegetables[2:4])
print(vegetables[len(vegetables)-1])
#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['ola', 32, 6.1, 'single', '14 Coldstream Avenue']
#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7 Print the list using print()
print(it_companies)
#8 Print the number of companies in the list
print(len(it_companies))
#9 Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[(len(it_companies)-1)])
#10 Print the list after modifying one of the companies
it_companies.pop(0)
it_companies.append('Infotech')
it_companies.insert(2, 'enhance IT')
print(it_companies)
#11 Add an IT company to it_companies
it_companies.append('sidmach')
it_companies.append('Infotech')
#12 Insert an IT company in the middle of the companies list
#it_companies.insert(2, 'enhance IT')
#13 Change one of the it_companies names to uppercase (IBM excluded!)
m_list = []

for i in it_companies:
    if i == 'Oracle':
        i = i.upper()
    m_list.append(i)
print(m_list)
#14 Join the it_companies with a string '#;  '
print('#'.join(it_companies))
#15 Check if a certain company exists in the it_companies list.
print('naija' in it_companies)
#16 Sort the list using sort() method
it_companies.sort()
#17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#18 Slice out the first 3 companies from the list
new_it_companies = it_companies[3:]
print(new_it_companies)
#19 Slice out the last 3 companies from the list
old_it_companies = it_companies[:-3]
print(old_it_companies)
#20 Slice out the middle IT company or companies from the list
it_count = len(it_companies)/2
print(it_companies[int(it_count)])
mid_it_companies = it_companies[5:6]
print(mid_it_companies)
#21 Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
#22 Remove the middle IT company or companies from the list
len_comp = len(it_companies)/2
it_companies.pop(4)
print(it_companies)
#23 Remove the last IT company from the list
it_companies.pop()
print(it_companies)
#24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#25 Destroy the IT companies list
del it_companies
#26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)
front_end.extend(back_end)
print(front_end)
#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
print(full_stack)

# Exercises: Level 2
#1 The following is a list of 10 students ages:
#Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
print(min_age,max_age)
#Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)
#Find the median age (one middle item or two middle items divided by two)
middle = len(ages)//2
print(ages[middle])
#Find the average age (sum of all items divided by their number )
ages_sum =sum(ages)
len_ages = len(ages)
avg_ages=(ages_sum/len_ages)
#Compare the value of (min - average) and (max - average), use abs() method
x = abs(min_age-avg_ages)
y = abs(max_age-avg_ages)
print(x,y)
print (x>y,x!=y, x is y)

#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
len_countries = len(countries)//2
print(countries[len_countries])
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_a = countries[0:96]
countries_b = countries[96:193]
print(countries_a)
print(countries_b)

#3 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,ru,us, *rest = country
print(ch, rest)
