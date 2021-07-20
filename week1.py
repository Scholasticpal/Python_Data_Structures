# STRINGS - A sequence of characters
# + means concatenate
# we prefer to read data using strings and then parse and convert the data as we need
# this gives us more control over error situations and/or bad user input
# input numbers must be converted from strings

# now let us look inside the strings:

# we can get at any single character in a string using an index using an index specified in square brackets
# The index value must be an integer and starts at zero:
#                banana
#                012345
# The index value can also be an expression that is computed

fruit = 'banana'
letter = fruit[1]     # [] square brackets are index operators
print(letter)

x = 3
w = fruit[x - 1]
print(w)

# you will get an error if you attempt to index beyond the end of the string
'''zot = 'abc'
print(zot[5])'''    # this will give an error

# len function gives us length of the string

fruit = 'banana'
print(len(fruit))

# looping through strings

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# for looping inside strings, a much more convenient way than above is using a for loop

fruit = 'banana'
for letter in fruit:
    print(letter)

# thus using definite loop is more convenient.

# looping and counting
# Q. Loop for counting no. of 'a' in the string 'banana'
word = 'banana'
count = 0
for letter in word:           # here 'letter' is the iteration variable
    if letter == 'a':
        count = count + 1
print(count)

# Slicing Strings
# Consider the string:
#                M O N T Y   P Y T H O N
#                0 1 2 3 4 5 6 7 8 9 1011
# we can look at any continuous section of a string using ':' colon operator
s = "MONTY PYTHON"
print(s[0:4])    # >> MONT
print(s[6:7])    # >> P
print(s[6:20])   # >> PYTHON
# note that the second number in the bracket is one beyond the end of slice - "up to but not including"
# if the second number is any number beyond the end of the string, it stops at the end.

# If we leave off the first number or the last number of the slice, it is assumed to be beginning or the end of the string respectively

s = 'MONTY PYTHON'
print(s[:2])    # >> MO
print(s[8:])    # >> THON
print(s[:])     # >> MONTY PYTHON

# using 'in' as logical operator
# it returns True or False and can be used in an if statement

fruit = 'banana'
if 'a' in fruit:
    print('found it')

if word == 'banana':
    print('alright, bananas.')
if word < 'banana':
    print('your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('your word,' + word + ',comes after banana')
else:
    print('alright, bananas.')
# in strings, <, > are related to importance and numbering of characters in python

# string library - it contains many inbuilt functions

greet = 'Hello Bob'
zap = greet.lower()               # .lower() is a built in function for strings
print(zap)
print(greet)
print('Hi There'.lower())

# NOTE - These functions do not modify the original string, instead they return a new string that has been altered

stuff = 'Hello world'
type(stuff)
print(dir(stuff)) # dir() tells us what all is a is the concerned variable capable of

# find() - used to find a substring within a string
# it returns -1 if the substring is not found
fruit = 'banana'
pos = 'banana'.find('na')
print(pos)      # here output is 2
aa = fruit.find('z')
print(aa)

#making everything UPPERCASE or lower case
greet = 'hello  Bob'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)
# we use this to use find() as python is case sensitive thus first we convert all to lowercase then usr find()

# replace() - Search and Replace
greet = 'hello bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o','x')
print(nstr)

# lstrip() - removes space from left i.e beginning
# rstrip() - removes spaces from right = ending
greet = '           Hello Bob       '
greet.lstrip()
greet.rstrip()
greet.strip()

# startswith() - tells us what string starts with
line = 'please have a nice day'
line.startswith("please") # OUTPUT is True
line.startswith('p')

# parsing and extracting
# consider the data given below:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# we want to extract uct.ac.za from the data above
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos) # output is 21 as '@' is on 21st position
sppos = data.find('',atpos) # this means that we are looking for ' ' strarting from atpos i.e. 21
print(sppos) # output is 31 as ' ' is on 31st position
host = data[atpos+1 : sppos]
print(host)  # Answer

# Assignment
# Q. Write code using find() and string slicing (see section 6.10) to extract the number
# at the end of the line below. Convert the extracted value to a floating point number and print it out.

# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
spot = text.find('')
host = text[spot+1:]
main = host.strip()
print(float(main))
