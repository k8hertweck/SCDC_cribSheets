#!/usr/bin/env python3

#### Software Carpentry Programming with Python ####

#### Before class ####

# ipython notebook located in Dropbox folder, render in nbviewer, share link to latter so students can follow along (and download notebook)
# check software installation: Python v 3.X (Anaconda)

#### Objectives ####

# why python?
#   We're teaching you how to program, and we have to use something
#   free, well documented, and everyone can run it
#   large userbase
#   easy for novices to learn
#   super popular on campus!
# motivation: inflammation in patients who have been given new treatment for arthritis
#   load data into memory, calculate average inflammation per day across all patients, plot to share info with colleagues
#   data: CSV, comma separated values
#   rows contain information for a single patient (observations)
#   columns represent measurements on successive days

#### Setup ####

# many ways to interact with Python
#   python in terminal
#   ipython in terminal
#   save script in text editor
#   IDE like spyder
#   notebook: web application that combines code, graphs, and text
#   interactive mode in terminal, chevrons (>>>) is prompt, waiting for input
#   scripting mode: save commands in file (ends in .py), execute entire file at once
# about our tools
#   Anaconda: distribution (way of obtaining) Python;
#       includes extra packages like ipython, spyder
#   conda: package manager that comes with Anaconda, installs/updates packages
#   jupyter notebook: installed with Anaconda

# setting up jupyter project
#   launch Jupyter Notebook from Anaconda
#   terminal window must stay open, this is kernel (running python)
#   web browser is how you interact with notebook
#   create project directory (new folder), rename, then move into it
#   click "New" in upper right hand, then select "Python3"
#   creates notebook (*.ipynb, or ipython notebook file)
#   autosaves, or can save manually
#   click on title to rename
# executing code in a jupyter notebook:
#   enter code in cell and execute by pressing Shift + Return/enter
#   output is printed directly below cell, prefaced by Out[ ]:
#   add new cell with + button
#   can add Markdown cells with nicely formatted text
#   comments prefaced with # (not read/executed by python)
#   commands and output saved in notebook
#   talk about other menu options and buttons to remove/add/run cells
#   example notebook: https://github.com/rasilab/machkovech_2018/blob/master/scripts/NA43_competition.ipynb

#### Analyzing patient data ####

# Objectives: intro to libraries, read in data, assign values to variables, select data values, operations on arrays, simple graphs

# include human-readable (but not python interpreted) comments following hash signs

# use python as calculator
3 + 5
# shift+enter to execute command

# assign value to variable
weight_kg = 60
# variable names:
#   can include letters, digits, and underscores
#   cannot start with a digit
#   are case sensitive

# data types:
#   integers
#   floating point numbers (decimals)
#   strings (characters)
# weight_kg is integer
# to create as floating point
weight_kg = 60.0
# to create string
weight_kg_text = 'weight in kilograms:'

# using variables
# display value of variable
print(weight_kg)
# print is a function
# can display multiple items at once
print(weight_kg_text, weight_kg)

# perform arithmetic inside print function
print('weight in pounds:', 2.2 * weight_kg)
# note: this doesn't change the value of weight_kg!
print(weight_kg)

# assign new value to weight_kg
weight_kg = 65.0
print('weight in kilograms is now:', weight_kg)
# variable names as sticky notes (analogy)

## Challenge: What values do the variables mass and age have after each statement in the following program? Test your answers by executing the commands.
mass = 47.5
age = 122
mass = mass * 2.0
age = age - 20
print(mass, age)

## Challenge: What does the following program print out?
first, second = 'Grace', 'Hopper'
third, fourth = second, first
print(third, fourth)

# libraries: collections of additional code that provide more functionality to perform specific tasks
# load library
import os
import urllib.request
import zipfile
import numpy

# download data
urllib.request.urlretrieve("http://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-data.zip", "python-novice-inflammation-data.zip")
# unzip data
zipData = zipfile.ZipFile('python-novice-inflammation-data.zip')
zipData.extractall()

# load data into python (using library)
numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
# numpy.loadtxt(...) is a function call
#   run function loadtxt
#   belongs to numpy library
#   dotted notation in function call means whatever appears before dot contains the thing after the dot
# parameters: specific information that is sent to (passed) to function call
#   name of file
#   delimiter

# assign data to variable (so we can recall it later)
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
# show the variable's value
print(data)
# what type of thing is data?
print(type(data))
# find type of data contained within array (data)
print(data.dtype)
# show shape of data
print(data.shape)
# output is rows, columns; rows are the individual patients, and the columns are their daily inflammation measurements
# arrays have members, or attributes, which use the dot nomenclature because they have the same part-and-whole relationship

# access a specific value
print('first value in data:', data[0, 0])
# python begins indexing (counting) at 0
print('middle value in data:', data[30, 20])

# select sections of data (slicing)
print(data[0:4, 0:10])
# end bound is NOT inclusive (up to but not including)
# can start at indeces besides 0
print(data[5:10, 0:10])
# use empty bound to include the end of axis
small = data[:3, 36:] # assign to value
print('small is:')
print(small)

# perform math on array
doubledata = data * 2.0
# view output
print('original:')
print(data[:3, 36:])
print('doubledata:')
print(doubledata[:3, 36:])

# perform operation involving two arrays
tripledata = doubledata + data
print('tripledata:')
print(tripledata[:3, 36:])

## Challenge: We can slice character strings as well! Given the following:
element = 'oxygen'
print('first three characters:', element[0:3])
print('last three characters:', element[3:6])
# What is the value of element[:4]? What about element[4:]? Or element[:]?
element[4:]
element[:]

## Challenge: What is element[-1]? What is element[-2]?
element[-1]
element[-2]

# Given those answers, explain what element[1:-1] does.
# Creates a substring from index 1 up to (not including) the final index, effectively removing the first and last letters from ‘oxygen’

# perform calculation across entire array
print(numpy.mean(data)) # find mean

# use multiple assignment to obtain descriptive values of data
maxval, minval, stdval = numpy.max(data), numpy.min(data), numpy.std(data)

print('maximum inflammation:', maxval)
print('minimum inflammation:', minval)
print('standard deviation:', stdval)

# to find available functions and information:
#   type name of something, followed by dot, then hit tab (ipython and notebooks)
#   select a function or attribute and add question mark to find help documentation
#   help(thing.attribute) is same as above

# view max inflammation per patient or per day
# create temporary array for data desired
patient_0 = data[0, :] # 0 on the first axis (rows), everything on the second (columns)
print('maximum inflammation for patient 0:', numpy.max(patient_0))

# combine selection and function call (skip temp variable)
print('maximum inflammation for patient 2:', numpy.max(data[2, :]))

# average across all rows (axis 0)
print(numpy.mean(data, axis=0))
# confirm shape of array
print(numpy.mean(data, axis=0).shape)
# average across all columns (axis 1): avg inflammation per day for all patients
print(numpy.mean(data, axis=1))

#### Visualizing data ####

# make pylot available from matplotlib (de facto plotting library)
import matplotlib.pyplot
# allow plots to appear when using show()
%matplotlib inline

# make heatmap from data
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()

# plot average inflammation over time
ave_inflammation = numpy.mean(data, axis=0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()

# plot max over time
max_plot = matplotlib.pyplot.plot(numpy.max(data, axis=0))
matplotlib.pyplot.show()

# plot min over time
min_plot = matplotlib.pyplot.plot(numpy.min(data, axis=0))
matplotlib.pyplot.show()

## Challenge: Create a plot showing the standard deviation (numpy.std) of the inflammation data for each day across all patients.
std_plot = matplotlib.pyplot.plot(numpy.std(data, axis=0))
matplotlib.pyplot.show()

# grouping plots: complete set of code

# load libraries
import numpy
import matplotlib.pyplot

# load data from file
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

# create space to place plot
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0)) # state dimensions of figure

# add subplots, parameters are number of subplots, number of columns, which subplot (left-to-right, top-to-bottom)
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

# title axes
axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

# spread out graphs
fig.tight_layout()

# show plot
matplotlib.pyplot.show()

## Challenge: Modify the program to display the three plots on top of one another instead of side by side.
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

# change figsize (swap width and height)
fig = matplotlib.pyplot.figure(figsize=(3.0, 10.0))

# change add_subplot (swap first two parameters)
axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()

matplotlib.pyplot.show()

## Challenge: How would you alter the limits on the x and y axes?
axes3.set_ylim(0,6)
# A more automated approach
min_data = numpy.min(data, axis=0)
axes3.set_ylabel('min')
axes3.plot(min_data)
axes3.set_ylim(numpy.min(min_data), numpy.max(min_data) * 1.1)

## Wrap up:
# some of our data appears suspicious (avg, max, and min has odd pattern)
# we want to re-run for all our datasets

#### Repeating actions with loops ####

# Objectives: write for loop to repeat simple actions, trace changes to variables

# what if we wanted to print each character in a word on a line of its own?
word = 'lead'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
# try a different word
# this doesn't scale well, and is fragile (creates error if word is shorter, doesn't print all for longer word)

# print with for loop
for char in word:
    print(char)
# syntax:
#   for variable in collection:
#       do things using variable
# note on choosing meaningful variable names

# for loop that repeatedly updates variable
length = 0 # define external variable
for vowel in 'aeiou': # initialize for loop for string (not variable)
    length = length + 1 # define continuously updated variable internal to loop
print('There are', length, 'vowels') # report output at end of loop

# loop variables still exist after loop ends!
letter = 'z'
for letter in 'abc':
    print(letter)
print('after the loop, letter is', letter)

# finding length of a string is a built-in function!
print(len('aeiou'))

## Challenge: Exponentiation is built into Python:
print(5 ** 3)
# Write a  loop that calculates the same result as 5 ** 3 using multiplication (and without exponentiation).
result = 1
for i in range(0, 3):
    result = result * 5
print(result)

#### Storing multiple values in lists ####

# Objectives: create and index lists of simple values, change values of elements, append to list, reorder and slice lists, create and manipulate nested lists

# a list if a way to store many values
# create a list
odds = [1, 3, 5, 7]
# recall list
print('odds are:', odds)
# select individual elements via indexing
print('first and last:', odds[0], odds[-1])
# loop over list (loop variable is assigned to elements one at a time)
for number in odds:
    print(number)
# you can change values in a list (but not individual characters in a string)
# list example
names = ['Curie', 'Darwing', 'Turing']  # typo in Darwin's name
print('names is originally:', names)
names[1] = 'Darwin'  # correct the name
print('final value of names:', names)
# string example
name = 'Darwin'
#name[0] = 'd'

# two variables can refer to the same list; modifying one modifies both!
salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_salsa = salsa        # <-- my_salsa and salsa point to the *same* list data in memory
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', my_salsa)

# a better way is to make a copy of the original list
salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_salsa = list(salsa)        # <-- makes a *copy* of the list
salsa[0] = 'hot peppers'
print('Ingredients in my salsa:', my_salsa)

# lists can contain other lists
x = [['pepper', 'zucchini', 'onion'],
     ['cabbage', 'lettuce', 'garlic'],
     ['apple', 'pear', 'banana']]
# print first row
print([x[0]])
print(x[0])
# print first item in first row
print(x[0][0])

# lists can contain elements of different types
sample_ages = [10, 12.5, 'Unknown']

# append to the list
odds.append(11)
print('odds after adding a value:', odds)

# remove first element
del odds[0]
print('odds after removing the first element:', odds)

# reverse the list
odds.reverse()
print('odds after reversing:', odds)

# demo: making a list and attempting to copy/modify in place is a bad idea!
odds = [1, 3, 5, 7]
primes = odds
primes.append(2)
print('primes:', primes)
print('odds:', odds)
# python stores a list in memory, and then can use multiple names to refer to the same list

# to copy a simple list, use list function
odds = [1, 3, 5, 7]
primes = list(odds)
primes.append(2)
print('primes:', primes)
print('odds:', odds)

## Challenge: Use a for-loop to convert the string “hello” into a list of letters: ["h", "e", "l", "l", "o"]
# Hint: you can create an empty list with: my_list = []
my_list = []
for char in "hello":
    my_list.append(char)
print(my_list)

# slicing lists
binomial_name = "Drosophila melanogaster"
group = binomial_name[0:10]
print("group:", group)

species = binomial_name[11:24]
print("species:", species)

chromosomes = ["X", "Y", "2", "3", "4"]
autosomes = chromosomes[2:5]
print("autosomes:", autosomes)

last = chromosomes[-1]
print("last:", last)

## Challenge: Use slicing to access only the last four characters of a string or entries of a list.
string_for_slicing = "Observation date: 02-Feb-2013"
list_for_slicing = [["fluorine", "F"],
                    ["chlorine", "Cl"],
                    ["bromine", "Br"],
                    ["iodine", "I"],
                    ["astatine", "At"]]
# Expected result:
#   "2013"
#   [["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]
string_for_slicing[-4:]
list_for_slicing[-4:]

# take a slice from the beginning of the sequence
# omit the first range to indicate the start
date = "Monday 4 January 2016"
day = date[0:6]
print("Using 0 to begin range:", day)
day = date[:6]
print("Omitting beginning index:", day)

# omit the last range to indicate the end
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
sond = months[8:12]
print("With known last position:", sond)
sond = months[8:len(months)]
print("Using len() to get last entry:", sond)
sond = months[8:]
print("Omitting ending index:", sond)

## Challenge: + usually means addition, but when used on strings or lists, it means “concatenate”. Given that, what do you think the multiplication operator * does on lists? In particular, what will be the output of the following code?
counts = [2, 4, 6, 8, 10]
repeats = counts * 2
print(repeats)
# [2, 4, 6, 8, 10, 2, 4, 6, 8, 10]: the multiplication operator * used on a list replicates elements of the list and concatenates them together and is equivalent to: counts + counts

#### Analyzing data from multiple files ####

# import library to find files/directories
import glob

# get names of all csv files in current directory
print(glob.glob('data/inflammation*.csv'))

# combine previous content together and analyze all files

import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob('data/inflammation*.csv'))
filenames = filenames[0:3]
for f in filenames:
    print(f)

    data = numpy.loadtxt(fname=f, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()

## Challenge: Plot the difference between the average of the first dataset and the average of the second dataset, i.e., the difference between the leftmost plot of the first two figures.
import glob
import numpy
import matplotlib.pyplot

filenames = sorted(glob.glob('data/inflammation*.csv'))

data0 = numpy.loadtxt(fname=filenames[0], delimiter=',')
data1 = numpy.loadtxt(fname=filenames[1], delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

matplotlib.pyplot.ylabel('Difference in average')
matplotlib.pyplot.plot(numpy.mean(data0, axis=0) - numpy.mean(data1, axis=0))

fig.tight_layout()
matplotlib.pyplot.show()

#### Making choices ####

# Objectives: write conditional statements including if, elif, else; evaluate expressions containing and and or

# tell python to take different actions with if statements
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')

# don't need else; can also do nothing
num = 53
print('before conditional...')
if num > 100:
    print(num,' is greater than 100')
print('...after conditional')

# can have multiple alternatives using elif
num = -3

if num > 0:
    print(num, 'is positive')
elif num == 0: # double equal sign is necessary; single used to assign values
    print(num, 'is zero')
else:
    print(num, 'is negative')

# combine tests using and, when both parts must be true
if (1 > 0) and (-1 > 0):
    print('both parts are true')
else:
    print('at least one part is false')

# combine tests using or if at least one part must be true
if (1 < 0) or (-1 < 0):
    print('at least one test is true')
# true and false are booleans

## Challenge: What do you expect to get from this code?
if 4 > 5:
    print('A')
elif 4 == 5:
    print('B')
elif 4 < 5:
    print('C')
# C gets printed because the first two conditions, 4 > 5 and 4 == 5, are not true, but 4 < 5 is true.

# checking for problems in inflammation data
import numpy # if not already done

# check if max inflammation equals day number (error in data entry)
max_inflammation_0 = numpy.max(data, axis=0)[0]
max_inflammation_20 = numpy.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')

# check if mins are all zero (healthy patient)
if numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')

# combine together with data
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

max_inflammation_0 = numpy.max(data, axis=0)[0]
max_inflammation_20 = numpy.max(data, axis=0)[20]

if max_inflammation_0 == 0 and max_inflammation_20 == 20:
    print('Suspicious looking maxima!')
elif numpy.sum(numpy.min(data, axis=0)) == 0:
    print('Minima add up to zero!')
else:
    print('Seems OK!')

## Challenge:
# Write a loop that counts the number of vowels in a character string.
# Test it on a few individual words and full sentences.
# Once you are done, compare your solution to your neighbor’s. Did you make the same decisions about how to handle the letter ‘y’ (which some people think is a vowel, and some do not)?
vowels = 'aeiouAEIOU'
sentence = 'Mary had a little lamb.'
count = 0
for char in sentence:
    if char in vowels:
        count += 1

print("The number of vowels in this string is " + str(count))

#### Creating functions ####

# Objectives: define new functions that takes parameters, return value from function, test and debug, set default values for function parameters

# functions allow us to create a shorthand way to re-execute longer pieces of code
# define function that converts temps from F to C
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))

# test function
fahr_to_celsius(32)
# we can use this the same way we use other functions
print('freezing point of water:', fahr_to_celsius(32), 'C')
print('boiling point of water:', fahr_to_celsius(212), 'C')

# composing functions
# write a function to convert C to K
def celsius_to_kelvin(temp_c):
    return temp_c + 273.15

print('freezing point of water in Kelvin:', celsius_to_kelvin(0.))

# convert F to K: compose the two functions we have already created (to apply one function to the result of another)
def fahr_to_kelvin(temp_f):
    temp_c = fahr_to_celsius(temp_f)
    temp_k = celsius_to_kelvin(temp_c)
    return temp_k

print('boiling point of water in Kelvin:', fahr_to_kelvin(212.0))

## Challenge: “Adding” two strings produces their concatenation: 'a' + 'b' is 'ab'. Write a function called fence that takes two parameters called original and wrapper and returns a new string that has the wrapper character at the beginning and end of the original. A call to your function should look like this:
# input: print(fence('name', '*'))
# output: *name*
def fence(original, wrapper):
    return wrapper + original + wrapper

## Challenge: Note that return and print are not interchangeable. print is a Python function that prints data to the screen. It enables us, users, see the data. return statement, on the other hand, makes data visible to the program. Let’s have a look at the following function:
def add(a, b):
    print(a + b)
# What will we see if we execute the following commands?
A = add(7, 3)
print(A)
# Python will first execute the function add with a = 7 and b = 3, and, therefore, print 10. However, because function add does not have a line that starts with return (no return “statement”), it will, by default, return nothing which, in Python world, is called None. Therefore, A will be assigned to None and the last line (print(A)) will print None. As a result, we will see:
#10
#NONE

# make inflammation process easier to read and reuse by defining code as function
def analyze(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(data, axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()

# make a function to find the problems we noticed earlier
def detect_problems(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif numpy.sum(numpy.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')

# we can run both at once across all files in a for loop
filenames = sorted(glob.glob('inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analyze(f)
    detect_problems(f)

# testing and documenting
# write a function to offset data (allows to test functions)
def offset_mean(data, target_mean_value):
    return (data - numpy.mean(data)) + target_mean_value

# create test matrix of 0s and offset values using new function (to test it)
z = numpy.zeros((2,2))
print(offset_mean(z, 3))

# use offset function on real data
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print(offset_mean(data, 0))

# confirm offset has worked
print('original min, mean, and max are:', numpy.min(data), numpy.mean(data), numpy.max(data))
offset_data = offset_mean(data, 0)
print('min, mean, and max of offset data are:',
      numpy.min(offset_data),
      numpy.mean(offset_data),
      numpy.max(offset_data))
# offset isn't exact, but is close

# check standard deviation
print('std dev before and after:', numpy.std(data), numpy.std(offset_data))
# check more precisely
print('difference in standard deviations before and after:',
      numpy.std(data) - numpy.std(offset_data))

# we could add documentation to offset function to describe its purpose using comments
# alternatively, add string to function itself, which embeds in help documentation
def offset_mean(data, target_mean_value):
    '''Return a new array containing the original data
       with its mean offset to match the desired value.'''
    return (data - numpy.mean(data)) + target_mean_value
help(offset_mean)
# docstring; triple quotes allows us to break into separate lines (and add example)
def offset_mean(data, target_mean_value):
    '''Return a new array containing the original data
       with its mean offset to match the desired value.
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + target_mean_value
help(offset_mean)

# defining defaults
# pass the filename to loadtxt without the fname=
numpy.loadtxt('inflammation-01.csv', delimiter=',')
# delimiter needs to be there!
numpy.loadtxt('inflammation-01.csv', ',')

# redefine offset mean
def offset_mean(data, target_mean_value=0.0):
    '''Return a new array containing the original data with its mean offset to match the
       desired value (0 by default).
    Example: offset_mean([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - numpy.mean(data)) + target_mean_value

# can still call function with two arguments
test_data = numpy.zeros((2, 2))
print(offset_mean(test_data, 3))

# call it with just one parameter, target_mean_value automatically assigned the default value of 0.0
more_data = 5 + numpy.zeros((2, 2))
print('data before mean offset:')
print(more_data)
print('offset data:')
print(offset_mean(more_data))

# how Python matches values to parameters:
def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)

print('no parameters:')
display()
print('one parameter:')
display(55)
print('two parameters:')
display(55, 66)

# override behavior by naming value as it's passed
print('only setting the value of c')
display(c=77)

# readable functions
# show example: http://swcarpentry.github.io/python-novice-inflammation/06-func/index.html

## Challenge: Return vs print

#### Errors and Exceptions ####

# example traceback
def favorite_ice_cream():
    ice_creams = [
        "chocolate",
        "vanilla",
        "strawberry"
    ]
    print(ice_creams[3])

favorite_ice_cream()

#syntax errors
# colon
#indentation

# variable name errors

# index errors

# file errors

#### Defensive programming ####

# are we getting the right answer?
#   Write programs that check their own operation.
#   Write and run tests for widely-used functions.
#   Make sure we know what “correct” actually means.

# assume mistakes will happen and guard against them (defensive programming)

# assertions: statement that something must be true at a certain point in a program
numbers = [1.5, 2.3, 0.7, -0.001, 4.4]
total = 0.0
for n in numbers:
    assert n > 0.0, 'Data should only contain positive values'
    total += n
print('total is:', total)
# types:
#   precondition is something that must be true at the start of a function in order for it to work correctly.
#   postcondition is something that the function guarantees is true when it finishes.
#   invariant is something that is always true at a particular point inside a piece of code.

# test driven development
# normal tendency is to do:
#   Write a function range_overlap.
#   Call it interactively on two or three different inputs.
#   If it produces the wrong answer, fix the function and re-run that test.
# better practice is to:
#   Write a short function for each test.
#   Write a range_overlap function that should pass those tests.
#   If range_overlap produces any wrong answers, fix it and re-run the test functions.

#### Debugging ####

# overview practices

## Challenge: pair up, introduce error, try to debug with applying principles

#### Command-line programs ####

# switch to command line
# download code file: http://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-code.zip
