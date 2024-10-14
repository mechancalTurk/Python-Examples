####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Types, Expressions & String Operations #######
####### B. Ege #######


type(777)
type(7.77)
type("Börtecin Ege")
type(True)

# System settings about float type
import sys
sys.float_info

# Converting from one object type to a different object type (typecasting)
# Verify that is an integer 
type(2)
# Convert 2 to a float
float(2)

# Convert integer 2 to a float and check its type
type(float(2))

# Casting 1.1 to integer will result in loss of information
int(1.1)

# Convert a string into an integer
int('1')
int("1")

# Convert the string "1.2" into a float
float(1.2)

# Convert an integer to a string
str(1)

# Convert a float to a string
str(1.2)

# Convert True to int
int(True)

# Convert 1 to boolean
bool(1)

# Convert 0 to boolean
bool(0)

# Convert True to float
float(True)

# What is the data type of the result of: 6 / 2?
type(6/2)

# What is the data type of the result of: 6 // 2?
type(6//2)

# Let's write an expression that calculates how many hours there are in 160 minutes: 
x = 160//60
print(x)

########################### STRING OPERATIONS ########################################

# Use quotation marks for defining string
print("Michael Jackson")

# We can also use single quotation marks:
print('Michael Jackson')

# A string can also be a combination of special characters:
print('@#2_#]&*^%$')

####### Indexing #######
# It is helpful to think of a string as an ordered sequence. 
# Each element in the sequence can be accessed using an index represented by the array of numbers:
name = "Michael Jackson"
print(name[0], name[8], name[14]);

# Print the last element in the string
print(name[-1])

# Print the first element in the string
print(name[-15])

# Find the length of string
print(len("Michael Jackson"))

######## SLICING (AUFSCHNEIDEN) ##########
# We can obtain multiple characters from a string using slicing, we can obtain the 0 to 4th 
# and 8th to the 12th element:
print(name[0:4])
print(name[8:12])

######### STRIDE ##########
# We can also input a stride value as follows, with the '2' indicating 
# that we are selecting every second variable:
# # Get every second element. The elements on index 1, 3, 5 ...
print(name[::2])
# We can also incorporate slicing with the stride. In this case, we select the first five elements 
# and then use the stride:
# Get every second element in the range from index 0 to index 4
print(name[0:5:2])

####### CONCATENATE TWO STRINGS ########
# We can concatenate or combine strings by using the addition symbols, 
# and the result is a new string that is a combination of both:
name = "Michael Jackson"
name = name + " is the best \n"
print(name)

print(3*name)

# Tab escape sequence
print(" Michael Jackson \t is the best")

# If you want to place a back slash in your string, use a double back slash:
print(" Michale Jackson \\ is the best")
# We can also place an "r" before the string to display the backslash:
print(r" Michael Jackson \ is the best")
print(" Michael Jackson \ is the best")   # kommt das Gleiche!!!

########### STRING MANIPULATION OPERATIONS ############

# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
print(b)

# The method find finds a sub-string. The argument is the substring you would like to find, 
# and the output is the first index of the sequence. We can find the sub-string jack or el.
# Find the substring in the string. Only the index of the first elment of substring in string will be the output:
name = "Michael Jackson"
position=name.find('el')
print(position)

position=name.find('Jack')
print(position)
position=name.find('jllack')
print(position)   # returns -1 it cannot find the substring

#Split the substring into list
name = "Michael Jackson"
split_string = (name.split())
print(split_string)


################### RegEx - REGULAR EXPRESSIONS ######################

# In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings.
# This RegEx module provides several functions for working with regular expressions, including search, split, 
# findall, and sub.
# Python provides a built-in module called re, which allows you to work with regular expressions. 
# First, import the re module
import re

s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"  
# Remember, we can also place an "r" before the string to display the backslash (line 119-120).

# Use the search() function to search for the pattern in the string 
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found:", result.group())
else:
    print("Match not found.")

# Regular expressions (RegEx) are patterns used to match and manipulate strings of text. 
# There are several special sequences in RegEx that can be used to match specific characters or patterns:
# \d Matches any digit character (0-9) "123" matches "\d\d\d"
# \D Matches any non-digit character "hello" matches "\D\D\D\D\D"
# \w Matches any word character (a-z, A-Z, 0-9, and _) "hello_world" matches "\w\w\w\w\w\w\w\w\w"
# \W Matches any non-word character "@#$%" matches "\W\W\W\W"
# \s Matches any whitespace character (space, tab, newline, etc.) "hello world" matches "\w\s\w\w\w\w\w"
# \S Matches any non-whitespace character "hello_world" matches "\S\S\S\S\S\S\S\S\S"
# \b Matches the boundary between a word character and a non-word character "cat" matches "\bcat\b" in "The cat sat on the mat"
# \B Matches any position that is not a word boundary "cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"

# Special Sequence Examples:
# A simple example of using the \d special sequence in a regular expression pattern with Python code:
pattern = r"\d\d\d\d\d\d\d\d\d\d"
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match.")
# The regular expression pattern is defined as r"\d\d\d\d\d\d\d\d\d\d", which uses the \d special sequence 
# to match any digit character (0-9), and the \d sequence is repeated ten times to match ten consecutive 
# digits

# A simple example of using the \W special sequence in a regular expression pattern with Python code:
pattern = r"\W"   # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)
print("Matches:", matches)
# The regular expression pattern is defined as r"\W", which uses the \W special sequence to match any character 
# that is not a word character (a-z, A-Z, 0-9, or _). The string we're searching for matches in is "Hello, world!".

# The findall() function finds all occurences of a specified pattern within a string:
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
result = re.findall("as", s2)
print(result)

split_array = re.split("\s", s2)
print(split_array)

# The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.
# Define the regular expression pattern to search for
pattern = r"King of Pop"
replacement = "legend"
new_string = re.sub(pattern, replacement, s2)
print(new_string)

############################  QUIZ ON STRINGS #################################
a = "1"
b = "2"
c = a+b
print(c)

a = 1
b = 2
c = a+b
print(c)

# Consider the variable d use slicing to print out the first three elements:
d = "ABCDEFG"
print(d[0:3])
print(d[:3])

# Use a stride value of 2 to print out every second character of the string e:
e = 'clocrkr1e1c1t'
print(e[::2])

# Print out a backslash:
print("\\")
print(r"\ ")
print("\\\\")

# Convert the variable f to uppercase:
f = "You are wrong"
print(f.upper())

# Convert the variable f to lowercase:
f2="YOU ARE RIGHT"
print(f2.lower())

# Consider the variable g, and find the first index of the sub-string snow:
g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
print(g.find("snow"))

# In the variable g, replace the sub-string Mary with Bob:
print(g.replace("Mary", "Bob"))

# In the variable g, replace the sub-string , with .:
print(g.replace(",", "."))

# In the string str1, replace the sub-string 'fox' with 'bear' using sub() function:
str1= "The quick brown fox jumps over the lazy dog."
print(re.sub(r"fox", "bear",str1))

# In the variable g, split the substring to list:
print(g.split())

# In the string s3, find whether the digit is present or not using the \d and search() function:
s3 = "House number- 1105"
match = re.search("\d", s3)
if match:
    print("Any number found:", match.group())
else:
    print("No match.")

# In the string str2 find all the occurrences of woo using findall() function:
str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
#re.compile(str2)
print(re.findall(r"woo", str2))






























































