# Files
# Opening a file
#         - Before we can open a file, we must tell python which file we are going to work with
#           and what we will be doing with the file
#         - This is done with open() function
#         - open() returns a "file handle" - a variable used to perform operations on the file
#         - Similar to "File-> Open" in a word processor

# Using open()
''' handle = open(filename,mode) '''      # fhandle = open('mbox.txt','r')
# returns a handle use to manipulate the file
# file name is a string
# mode are optional.
#        r - if we are planning to read the file
#        w - if we are going to write to the file
#  default - if nothing is mentioned, read only is opened

# what is handle?
# it helps you open, write, read or close a file.
# ----------------------------------------------------------------------------------------------------------------------

# newline character
# this special character indicates when a line ends
# its is represented as \n in strings
# \n is counted as a single character

stuff = 'hello \nworld'
print(len(stuff))
print(stuff)
stuff = 'X\nY'
print(stuff)
print(len(stuff))
# ----------------------------------------------------------------------------------------------------------------------


xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
# A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
# we can use the for statement to iterate through a sequence
# remember - a sequence is an ordered set

# counting lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line count: ', count)

#reading the *whole* file
fhand = open('mbox.txt')
inp = fhand.read()       # using .read we can read the whole file (newlines and all) into a single string
print(len(inp))
print(inp[:29])

# we can put if statement in for loop to only print lines that meet some criteria

fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('m'):
        print(line)
# in the output of the above code, we can see there is one line gap between all the lines printed.
# to remove that gap we use rstrip() that removes white space from the right hand side of the lines. Newline is considered
# as a white space
      #  line = line.rstrip()
# we can conveniently skip a line by using continue statement
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('m'):
        continue
    print(line)

# Using in to Select lines
# we can look for a string anywhere in a line as our selection criteria
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not 'me' in line :
        continue
    print(line)

# how to read and write the name of the file
fname = input('Enter the name of the file: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('d'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# how to deal with incorrect file names?
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cant be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
        print('There were', count, 'subject lines in', fname)

# Assignment
# Q. Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    big = line.upper()
    best = big.rstrip()
    print(best)

# Q. Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#      X-DSPAM-Confidence:    0.8475
#    Count these lines and extract the floating point values from each of the lines and compute the average of those
#    values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ez = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        for re in line:
            if re.startswith("0."):
                num = float(line[re:])
                ez = ez + num
                count = count + 1
    print(line)
print(ez/count)
print("Done")
