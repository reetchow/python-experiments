# Data types

print('Data types')

print(4) # Integers (whole numbers)
print(6.78) # Floating point (decimal numbers)

print('hello my name is reet') # Strings (text)
print("welcome to python") # Strings (text)

print(True) # Booleans (true or false value)
print(False)

# Variables

print('Variables')

x = 10 # Declaration and Initialization
print('x =', x)
x = 30 # Reassignment
print('x =', x)

my_variable1 = 'hello jason'
my_floating_point = 6.54
my_condition = True

print(my_variable1)
print(my_floating_point)
print(my_condition)

# Math operations
print('Basic math operations')
x = 10
y = 15
print('x =', x, 'y =', y)
print(x + y) # Add
print(x - y) # Subtract
print(x * y) # Multiply
print(x / y) # Divide
print(x ** y) # Exponent
print('x =', x, 'y =', y)

# Shorthand reassignment
print('Shorthand reassignment')
x = 10
y = 5

# x = x + y
x += y
print(x)

x = 10
# x = x - y
x -= y
print(x)

x = 10
# x = x * y
x *= y
print(x)

x = 10
# x = x / y
x /= y
print(x)

# Functions
# To declare a function
print('Defining and calling a function')
def multiply(a, b):
	c = a * b
	return c # Returned a value

print(multiply(12, 10))

# Scope
# If I'm a variable, what can see me?
# Global Scope
# Local Scope
# Python uses indentation to represent scope

print('Hard coded count from 0 to 5')
a = 0
print(a)
a = 1
print(a)
a = 2
print(a)
a = 3
print(a)
a = 4
print(a)
a = 5
print(a)

# Looping
print('Looping count from 0 to 5')
for i in range(6):
	print(i)

# Homework

# problems defining variables
# math operations
# making a basic function
# simple loops
# something on the range function