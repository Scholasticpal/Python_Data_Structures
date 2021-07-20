# Pyhton Data Structures
# WEEK 5
# DICTIONARIES
# ----------------------------------------------------------------------------------------------------------------------
# What is not a Collection?
# Most of our variable have one value in them, when we put a new value in the variable, the old value is overwritten
x = 2
print(x)
x = 4
print(x)

# List - A linear collection of values that stays in order
# Dictionaries - A "bag" of values each with its own label

# keyword- Associative array
# ----------------------------------------------------------------------------------------------------------------------

# DICTIONARIES
# 1. Dictionaries are pythons most powerful data collection
# 2. Dictionaries allow us to do fast database-like operations in python
# 3. Dictionaries have different names in different languages -
#           - Associative arrays: Perl/PHP
#           - Properties or Map or HashMap: Java
#           - Property Bag: C#/.Net

# ----------------------------------------------------------------------------------------------------------------------

# Lists index their entries based in the position in the list but dictionaries are like bags - no order
# So we index the things we put in the dictionary with a lookup tag.

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)            # {'money': 12, 'tissues' : 75, 'candy' : 3} -> This order in which the output comes is random
print(purse['candy'])   # 3
purse['candy'] = purse['candy'] + 2
print(purse)

# ----------------------------------------------------------------------------------------------------------------------

# list vs Dictionaries
# list
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

# here, list
#  Key     Value
#  [0]      21
#  [1]      183

# Dictionary
ddd = dict()
ddd['age'] = 21
ddd['course'] = 183
print(lst)
lst[0] = 23
print(lst)

# here, dictionary
#   Key       Value
# ['course']   183
# ['age']      21

# ----------------------------------------------------------------------------------------------------------------------
# Dictionary Literals (Constants)

# Dictionary ltierals use curly braces and have a list of key : value pairs.
# you can also make an empty dictionary using curly braces

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)          # {'chuck' : 1, 'fred' : 42, 'jan' : 100}
ooo = { }
print(ooo)          # { }

# ----------------------------------------------------------------------------------------------------------------------
# Many Counters with a Dictionary
# Histogram Problem
# Q. How many of a selected thing exits? (word counting)

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['csev'] + 1
print(ccc)

# Dictionary Traceback

ccc = dict()
'''print(ccc['csev'])'''    # it is an error to  sefernce a key which is not in dictionary]

# When we see a new name
# When we encounter a new name, we need to add a new entry in the dictionary and if this is the second or later time we
# have seen the name, we simply add one to the count in the dictionary under that name.

counts = dict()
names = ['cesv', 'cwen', 'csev', 'zqain', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
# ----------------------------------------------------------------------------------------------------------------------

# The get method for dictionaries
# The pattern of cheking to see if a key is already in a dictionary and assuming a default value if the key is not there
# is so common that there is a method called get() that does this for us

if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)

# Simplified counting with get()

counts = dict()
names = ['csev', 'cwen', 'zqain', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) +1
    print(counts)

# ----------------------------------------------------------------------------------------------------------------------
# Counting Pattern (program to input lines and count each type of word present)
counting = dict()
print('Enter a line of text')
line = input('')
words = line.split()
print('words:', words)

print('Counting ...')
for word in words:
    counting[word] = counting.get(word, 0) + 1
print('Counts:', counting)

# ----------------------------------------------------------------------------------------------------------------------
# Definite Loops and dictionaries
# even though dictionaries are not stored in order, for loop can be used to go through all keys and look up the values

diction = {'chuck': 1, 'fred': 41, 'jan': 100}
for key in diction:
    print(key, diction[key])

# Retrieving lists of keys and values
# You can get a list of keys, values or items(both) from a dictionary
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))            # >>> ['jan', 'chuck', 'jan']
print(jjj.keys())           # >>> ['jan', 'chuck', 'jan']
print(jjj.values())         # >>> [100, 1, 42]
print(jjj.items())          # >>> [('jan',100), ('chuck',1), ('fred', 42)]  >these are tuples

# ----------------------------------------------------------------------------------------------------------------------
# Bonus: Two Iteration Variables!!!!

# We loop through the key-value pairs in a dictionary using *two* iteration variables
# Each iteration, first is the key and second is the corresponding value for the key
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa,bbb in jjj.items() :
    print(aaa,bbb)
# ----------------------------------------------------------------------------------------------------------------------
# Q. Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
#    messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
#    mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
#    they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
#    loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
words = list()
mail = dict()
handle = open(name)
for line in handle:
    words = line.split()
    for word in words:
        if word == 'From':
            mail[words[1]] = mail.get(words[1], 0) + 1
for key in mail:
        if mail.values() == max(mail.values()):
            print(key, mail[key])
        else:
            continue





