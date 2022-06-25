# variable = 'hello world'
# print(variable)

name = 'Woodard'
print(name)


# comment

'''
I am also a comment
except multi line
'''

"""
I, too, am a multi
line comment
"""

'''
Data Types

Text:   str
Numeric: int, float, complex
Sequence: list, tuple, range
Mapping: dict
Set:   set, frozenset
Boolean: bool
Binary: bytes, bytearray, memoryview

'''

single = 'python'
print(single)

double = "python1"
print(double)

triple = '''Used to wrap multiline strings like lorem
and I don't know what to say to fill this up. But, I'm
trying. Not very well, as you can see.'''
print(triple)

num = '123456780'
print(type(num))

numNum = 12345678
print(type(numNum))

var = '123456'
print(var.isdigit())  # true

print(var.isnumeric())  # false

var1 = 'python is powerful and I love it'
print(var1.islower())  # true  checks if all lowercase

var2 = 'python is \n powerful.'
print(var2.isprintable())  # false --- checks to see if all characters in string are printable - escape characters aren't

var3 = ' '
print(var3.isspace())  # true --- checks if string is only whitespace

var4 = 'python is powerful'
print(var4.istitle())  # false --- checks if string is title case

var5 = 'Python is powerful'
print(var5.istitle()) # false

var6 = 'Python Is Powerful'
print(var6.istitle()) # true 

var7 = 'PYTHON IS POWERFUL'
print(var7.isupper()) # true checks if all uppercase

var8 = 'PYTHON IS POWERFUL'
print(var8.lower()) # converts to lowercase

var9 = ',,,,,+++++++++,,,,I love Python'
print(var9.strip(', +')) # removes leading and trailing whitespace, unless chars are specified

var10 = 'I like Python'
# print(var10.replace(''))  # TypeError: replace() takes exactly 2 arguments (1 given)
print(var10.replace('Python', 'Ruby')) #  I like Ruby           replaces all instances of Python with Ruby

var11 = 'I like Python because it is powerful'
print(var11.rpartition('Python')) # ('I like ', 'Python', ' because it is powerful') Partition the string into three parts using the given separator.

var12 = 'I like Python because it is powerful'
print(var12.rstrip('Python')) # I like Python because it is powerful removes trailing whitespace unless characters are specified

var13 = 'I like Python because it is powerful'
# print(var13.splitlines()) # ['I like Python because it is powerful'] splits string into a list of strings, each of which is a line of text
print(var13.split(' ')) # ['I', 'like', 'Python', 'because', 'it', 'is', 'powerful'] splits string into a list of strings, each of which is a word of text

var14 = 'I like Python because it is powerful'
print(var14.startswith('I')) # true checks if string starts with the given string

var15 = 'Python because it is powerful'
print(var15.startswith('Python')) # true checks if string starts with the given string - case sensitive


var16 = 'I like Python because it is powerful'
print(var16.swapcase()) # I LIKE pYTHON BECAUSE IT IS POWERFUL converts all uppercase characters to lowercase and vice versa

var17 = 'I like Python because it is powerful'
print(var17.title()) # I Like Python Because It Is Powerful converts first letter of each word to uppercase

#Python numbers

a = 1
b = 2.1
c = 2+3j
print(type(a))  #int
print(type(b))  #float
print(type(c))  #complex number

#casting

print(int(b))  #2 changes to integer
print(float(a))  #1.0 changes to floating
print(complex(a))  # 1+0j changes to complex number

import random     #standard package from python library


print(random.randrange(1, 1000))   #generates random number within given range


# decimal to binary conversion










