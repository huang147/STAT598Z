# Examples to show basic Python syntax 
# Also see http://www.sthurlow.com/python/lesson02/ for a gentle Python
# tutorial 

# Mandatory Hello World
print "Hello, world"

# Using a "," supresses printing of a new line  
print "Hello, world",
print "Lets try this"

# Note that any line which starts with a # is ignored by the Python
# interpreter  

# Python Can do basic arithmetic just like a calculator
print 2+3
print "2+3 =", 2+3 # pretty formatting 
print 2-3
print 2*3
print 13/3 # Integer division 
print 2.0/3.0 # Now we get floating point division  
print 13*1.0/3
print 13%3 # remainder
print 2**3 # power

# Using paranthesis to delimit what you exactly mean
# is always a good programming practice 
print (3*(13/3))+(13**3)

# Lots of simple built in functions
import math
print math.log(100)
print math.log(100, 10) # 2nd argument is the base of the log 

# For other math functions please see http://docs.python.org/library/math.html

# You can store the results of your computation into variables
x=2+3
print x

# Variables can be of any type
y="this is a string"
print y

# You can assign a variable to a new type on the fly 
y=21
print y

# You can perform operations with variables
print x+y, x*y

# But you cannot mix operations on variables!
x="string"
y=21
# print x+y
# you can however print them side by side
print x, y

# When working with strings python does sensible things
x="string 1"
y=" string 2"
print x + y

# You can create a string using either double quotes " " or single
# quotes ' ' 

my_name='vishy'
print my_name

my_name="vishy"
print my_name

# To read input from the user use the raw_input function
x=raw_input("please enter an year:")
print x

# Python can be used to do fancy printing 
# See http://docs.python.org/library/string.html for detailed
# documentation

a=10
b=20
# {0} refers to the first argument to the format function {1} to the
# second argument and so on
print "first argument to format is {0} and second argument is {1}".format(a, b)

# Format a and b as floating point numbers
print "a={0:f}, b={1:f}".format(a, b)

# Format a and b as floating point numbers with fixed precision 
print "a={0:.2f}, b={1:.3f}".format(a, b)

# Format a and b as floating point numbers using exponent notation
print "a={0:e}, b={1:e}".format(a, b)

# Format a and b as integers 
print "a={0:d}, b={1:d}".format(a, b)

# Formatting a string and an integer
my_name="mark"
my_age=15
print "my name is {0} and my age is {1}".format(my_name, my_age)

# Note that this is also an alternate way to print things 
print "my name is " + my_name + " and my age is ", my_age

# Some notes:
# 
#
# To get help about a python command from within emacs just type
# Control-c Control-f  
# 
# For interactive help within the Python shell use
# help()
#
# To find out more about a topic type 
# help("topic")
# 
# To exit help type quit 
#
# Alternatively use ipython. It is a user friendly shell for Python. 
# 

