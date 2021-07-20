#                                                   PROGRAMMING
#         1. Algorithms - set of rules used to solve a problem
#         2. Data Structures - A particular way of organizing data in a computer

# Some types of data structures:
#        - Lists
#        - Dictionaries
#        - Tuples
# these are all some types of collections, i.e. they allow us to put many values in a single variable
#-----------------------------------------------------------------------------------------------------------------------

# List - it is a kind of collection.
friends = ['Joseph', 'Glenn', 'Sally']

# list constants are surrounded by [] brackets and the elements in the list are surrounded by commas
# a list constant can be any python object, even another list
# a list can be empty

print([3, 4,23])
print(['red, yellow', 'blue'])
print(['red', 24.56, 3])
print([1, [5,6], 7])   # this list also contains only 3 elements
print([])


for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')


# looking inside lists


# just like strings, we can get any single element in a list using an index specified in square brackets

friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])
#-----------------------------------------------------------------------------------------------------------------------

# Lists are mutable:
# Strings  are "immutable" - we cannot change the contents of a string - we must make a new string to make any changes
# lists are "mutable" - we can change an element of a list using the index operator

fruit = 'Banana'
# fruit[0] = 'b' will give error as we can change strings. even wgen we make the strings lowercase, we make a new string to save it.
x = fruit.lower()
print(x)
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

#-----------------------------------------------------------------------------------------------------------------------

# for length of a list, we use len()
greet = 'hello bob'
print(len(greet))
x = [1, 2, 'joe', 99]
print(len(x))    # output is 4

#-----------------------------------------------------------------------------------------------------------------------

# range() function
# The range function returns a list of numbers from zero to one less than the parameter
# we can construct an index loop using for and an integer iterator

print(range(4))           # output is [0, 1, 2, 3]
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))       # output is [0, 1, 2]
# ----------------------------------------------------------------------------------------------------------------------

# Concatenate lists using +
# we can create a new list by adding two lists together

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # output is [1, 2, 3, 4, 5, 6]

#-----------------------------------------------------------------------------------------------------------------------
# list can be sliced using:
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
# just like in strings, the second number is "up to but not including"
#-----------------------------------------------------------------------------------------------------------------------

# list methods
x = list()
type(x)
dir(x)
#-----------------------------------------------------------------------------------------------------------------------

# append() - building a list from scratch

# we can create an empty list and then add elements using the append method
# list stays in order and new elements are added at the end of the list

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# do not do this like we did in strings: x = x.append('cookie')
#-----------------------------------------------------------------------------------------------------------------------

# is something in a list?
# Python provides two operators that let you check if an item is in a list
# these are logical operators that return True or False
# They do not modify the list

lst = [1, 9, 21, 10, 16]
if 9 in lst:
    print(True)
else:
    print(False)

#-----------------------------------------------------------------------------------------------------------------------

# Lists are in Order
# Lists can be SORTED ( i.e. change its order)

# using .sort() :-
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[0])

#-----------------------------------------------------------------------------------------------------------------------

# some other built-in functions

nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) # 6
print(max(nums)) # 74
print(min(nums)) # 3
print(sum(nums)) # 154
print(sum(nums)/len(nums)) # 25.6

#-----------------------------------------------------------------------------------------------------------------------

# Best Friends: Strings and Lists


abc = 'With three words'   # a String
stuff = abc.split()        # ['With', 'three', 'words']  stuff is a list
print(stuff)
print(len(stuff))
print(stuff[0])
print(stuff)
for w in stuff:
    print(w)
# Split breaks a string into parts and produces a list of strings. We think of these as words.We can access a particular loop through all the words.
# This is how we take a string, split it into parts to look at an individual word.

# some other properties of split()

line = 'A lot                              of spaces'
etc = line.split()
print(etc)               # ['A', 'lot', 'of', 'spaces']
line = 'first;second;third'
thing = line.split()
print(thing)             # ['first';'second';'third']
print(len(thing))        # 1
thing = line.split(';')
print(thing)             # ['first', 'second', 'third']
print(len(thing))        # 3
# when you do not specify a delimiter, split split on the basis of spaces, counting multiple spaces as one.
#  you can specify what character you want to use in splitting

# ----------------------------------------------------------------------------------------------------------------------

# Double split pattern
# sometimes we split in one way, and then grab one of the pieces of the line and split that piece again
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])
# ----------------------------------------------------------------------------------------------------------------------

# Q. Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From '
#    like the following line:
#       From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#    You will parse the From line using split() and print out the second word in the line (i.e. the entire address of
#    the person who sent the message). Then print out a count at the end.
#    Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output
#    to see how to print the count.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1:
        continue
    if wds[0] != 'From':
        continue
    print(wds[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
