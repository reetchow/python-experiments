# Print Statements
print('hi!')
print(12354)
print('this is a number:', 901)

# Variables
# Think of them like a box that holds something
a = 1
print(a)
a = 2 # Reassignment
print(a)

# Data Types

# Strings (lines of text and characters)
my_string = 'hey my name\'s Reet!'
my_string2 = "and I <3 python3"
my_other_string = '''this's a triple quote string'''
last_string = """this is the other way to define and assign a string"""

# Numbers (Good ol' numericals
x = 213 # Integer
pi = 3.14159 # Floating point (decimal point numbers)
e = 2.7

# Booleans (wut?)
# Named after George Boole, some old mathematician who came up with Boolean Algebra
# Basically a true (1) or false (0) value
my_condition = False
my_other_condition = True

# We didn't get around to this so we'll talk about it next time
my_last_condition = my_condition and my_other_condition
my_last_condition = False and True

# variables

# data types (number, string, boolean, list)

# functions
# 	- definitions (def keyword)
# 	- calling a function

def multiply(a, b):
	return a * b

multiply(12, 5) # 60

# scope (what sees what)
# things inside functions CAN see the scope around them
# things outside functions CANNOT see into the function

# lists
my_list = [1, 2, 3, 4, 5]
my_other_list = ['hello', 'my', 'name', 'is', 'reet']
my_other_other_list = [5, 'my', True, 'is', 'reet'] # uncommon and probably bad practice
my_multidim_list =  [[1, 2, 3, 4, 5],
				[1, 2, 3, 4, 5],
				[1, 2, 3, 4, 5],
				[1, 2, 3, 4, 5],
				[1, 2, 3, 4, 5]]

# accessing list elements
my_list[0] # 1
my_list[1] # 2
my_list[2] # 3
my_list[3] # 4
my_list[4] # 5

# loops
# common in other languages
# initialization, condition, incrementation
index = 0
while(index < 5):
	print(my_other_list[index])
	index += 1

# Phew! Finally got through all that