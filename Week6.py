# Python Data Structures
# Week 6

# Tuples
# Tuples are another kind of sequence that functions much like a list - they have elements which indexed starting at 0

x = ('Glenn', 'Sally', 'Joseph')  # this is a three tuple because it has three things
print(x[2])                       # Joseph
y = (1, 9, 2)
print(y)                          # Output: (1, 9, 2) no square braces, instead parenthesis
print(max(y))
for iter in y:
    print(iter)

# but unlike lists, once you create a tuple, you cannot alter its contents - similar to a string

x = [9, 8, 7]      # LIST
x[2] = 6
print(x)

y = 'ABC'         # STRING
'''y[2] = 'D'''   # This will give a traceback error

z = (5, 4, 3)     # TUPLE
''' z[2] = 0 '''  # This will give a traceback error
# ----------------------------------------------------------------------------------------------------------------------

# NOTE - Also, you cant sort/ append/ reverse a tuple:
# x = (3, 2, 1)
# x.sort()
# x.append()
# x.reverse()

# To compare between the functions we can perform of list vs Tuple, use directory:
l = list()
dir(l)

t = tuple()
dir(t)

# ----------------------------------------------------------------------------------------------------------------------
# Tuples are more efficient

# 1. Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficientin terms
#    of memory use and performance than lists.
# 2. So in our program, we are making "temporary variables". we prefer tuples over lists.

# ----------------------------------------------------------------------------------------------------------------------
# tuple can also put a tuple on the left-hand side of an assignment statement
# we can even omit the parentheses
(x, y) = (4, 'fred')
print(y)                # output: fred
(a, b) = (99, 98)
print(a)                # output: 99

# (a, b) = 9 will give an error

# ----------------------------------------------------------------------------------------------------------------------
# Tuple and Assignment
# the items() method in dictionaries returns a list of (key, value) tuple

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items() :
    print(k, v)                # output: csev 2   cwen 4

tups = d.items()
print(tups)                    # output: dict_items([('csev', 2), ('cwen', 4)])

# ----------------------------------------------------------------------------------------------------------------------
# Tuples are comparable

# The comparison operator work with tuples and other sequences. If the first item is equal, Python goes to next element,
# and so on, until it finds the elements that differ.

(0, 1, 2) < (5, 1, 2)
(0, 1, 200000000) < (0, 3, 4)
('Jones', 'Sally') < ('Jones', 'Sam')             # This is true as l and m are compared from Sally and Sam
('Jones', 'Sally') > ('Adams', 'Sam')

# ----------------------------------------------------------------------------------------------------------------------
# Sorting Lists of Tuples

# We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary
# First we sort the dictionary by the key using the items() method and sorting function()

d = {'a': 10, 'b': 1, 'c': 22 }
d.items()             # return dict_items([('a', 10), ('c', 22), ('b', 1)])
sorted(d.items())     # return

# NOTE *** - you cannot put same key in a dictionary more than once. You can put same value but not key more than once.

# Using Sorted()

lss = [('a', 10), ('b', 1), ('c', 22)]
t = sorted(lss.items())
print(t)

for k, v in sorted(lss.items()):
    print(k, v)
# a 10
# b 1
# c 22

# Sort by Values instead of keys

# If we could construct a list of tuples of the form (value, key) we could sort by value
# we do this with a for loop that creates a list of tuples

c = {'a': 10, 'b': 1, 'c': 22 }
tmp = list()
for k, v in c.items():
    tmp.append((v, k))

print(tmp)       # [(10, 'a'), (22, 'c'), (1, 'b')]
tmp = sorted(tmp, reverse=True)
print(tmp)       # [(22, 'c'), (10, 'a'), (1, 'b')]

# ----------------------------------------------------------------------------------------------------------------------
# Q. Code for Top 10 most common words.

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()                             # start
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for val, key in lst[:10]:
    print(key, val)                      # end

# Now. We can do the while part from ' start' to 'end' in one line of code:

c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()]))              # put reverse = True in sorted() to print in key, value order
# output: [(1, 'b'), (10,'a'), ('22', 'c')]

# List comprehension, makes a dynamic list. In this case we made a list of reversed tuples and then sort it.
# [(v, k) for k, v in c.items()] - This whole is a list, that is in the form of an expression
# This is known as LIST COMPREHENSION
# ----------------------------------------------------------------------------------------------------------------------
