# Usually we want to logically group several statements which solve a
# common problem. One way to achieve that in Python is to use
# functions. Below we will show several features of functions in Python.  
# Some examples are from: http://secant.cs.purdue.edu/cs190c:notes09

# A simple function definition begins with the keyword def followed by
# name of the function followed by the arguments to the function in
# paranthesis. Also note the : and the indentation. Python is sensitive
# to indentation!

def hello_world():
    print "hello world"
    return

hello_world()

# We can customize the behavior of our functions by using parameters 
def greet(person):
    print "Hello " + person
    print "How are you?"
    return

greet("vishy")
greet("mark")
greet(1)

def mean(a, b):
    c=(a+b)/2.0
    return c

d=mean(2, 3)
print d
mean(2, 3)

# invoking the function 
print mean(3, 4)
print mean(5, 9)

def pass_by_value(a):
    a=20
    return

b=10
print "before calling pass_by_value:", b
pass_by_value(b)
print "after calling pass_by_value:", b

a=15
print "before calling pass_by_value:", a
pass_by_value(a)
print "after calling pass_by_value:", a

def multiple_args_return(a):
    b=2*a
    c=3*a
    return b, c, "hello"

x=10
y,z,a=multiple_args_return(x)
print y, z, a

def named_args(a,b):
    return b+2*a

named_args(b=10,a=12)
named_args(a=12,b=10)


def default_args(a, b=10):
    return b+2*a

default_args(12, 1)
default_args(12)

# This example shows recursion that is the ability of a function to call
# itself 
def fibonacci(n):
    if n>1:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return n

print fibonacci(1)
print fibonacci(5)
print fibonacci(10)
